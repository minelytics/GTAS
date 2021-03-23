#Create a synthetic cuscar edifact message of various sizes

__author__ = "Chris Humphreys"
__version__ = "1.0.0"
__license__ = "GPL3"

from pydifact.segmentcollection import SegmentCollection
from pydifact.segments import Segment
import string
import random
from datetime import datetime, timedelta
from pathlib import Path
import argparse

def random_string(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

#UNB+UNOB:2+SENDER+RECIPIENT+191021:1052+SRC-000001'
#UNH+MREF123456+CUSCAR:D:95B:UN:LOT10'
#BGM+85+DOCREF1234+9'
def add_headers(message : SegmentCollection, message_data : dict):
    message.add_segment(Segment("UNB", ["UNOB", "2"], message_data['sender_identification'], 
        message_data['recipient_identification'], [message_data['send_date'], message_data['send_time']], 
        message_data['interchangeControlReference']))
    message.add_segment(Segment("UNH", message_data['message_reference_number'], ["CUSCAR", "D", "95B", "UN", "LOT10"]))    
    message.add_segment(Segment("BGM", "85", message_data['document_reference_number'], "9"))

#UNT+313+MREF123456'
#UNZ+1+SRC-000001'
def add_footer(message : SegmentCollection, message_data : dict):
    number_of_segments = len(message.segments)
    message.add_segment(Segment("UNT", str(number_of_segments), message_data['message_reference_number']))
    message.add_segment(Segment("UNZ", "1", message_data['interchangeControlReference'])) 
    pass

#DTM+137:201910210852:203'
#RFF+SS:AREF1234567A'
#NAD+MS+SCR:172:20'
def add_cargo_report_sender_info(message : SegmentCollection, message_data : dict):
    message.add_segment(Segment("DTM", [ "137", message_data['submit_to_customs_timestamp'], "203"]))
    message.add_segment(Segment("RFF", ["SS", message_data['sellers_message_reference_number']]))
    message.add_segment(Segment("NAD", "MS", [message_data['sender_identification'], "172", "20"]))

#TDT+20+TRANS1234+1++SENDER:172:20:SOMEONE+++MEANSTRANS1234:103::TEST SHIP'
#LOC+60+GBPME::139'
#DTM+132:201910290330:203'
#DTM+232:201910290330:203'
def add_details_of_transport_and_arrival(message : SegmentCollection, message_data : dict):
    message.add_segment(Segment("TDT", "20", message_data['conveyance_reference_number'], "1", None, 
        [ message_data['sender_identification'], "172", "20", message_data['carrier_name']], None, None, 
        [message_data['means_of_transport_identification'], "103", None, message_data['means_of_transport']]))
    message.add_segment(Segment("LOC", "60", [message_data['arrival_port'], None, "139"]))
    message.add_segment(Segment("DTM", [ "132", message_data['arrival_datetime_estimated'], "203"]))
    message.add_segment(Segment("DTM", [ "232", message_data['arrival_datetime_scheduled'], "203"]))

#GIS+23'
def add_general_indicator(message : SegmentCollection, message_data : dict):
    message.add_segment(Segment("GIS", "23"))

#EQD+BL+EQ123456+7:ZZZ:5++3+5'
#MEA+AAE+G+KGM:55814'
#MEA+AAE+AAW+MTQ:0'
def add_equipment(message : SegmentCollection, equipment_data : dict):
    #Blocks, refrigerated tank
    message.add_segment(Segment("EQD","BL", equipment_data['identification_number'],["7", "ZZZ", "5"], None, "3", "5"))
    message.add_segment(Segment("MEA","AAE", "G", ["KGM", equipment_data['total_gross_weight']])) # weight
    message.add_segment(Segment("MEA","AAE", "AAW", ["MTQ", "100" ])) # volume
    
def add_consigments(message : SegmentCollection, message_data : dict):
    consignments = message_data['consignments']
    for consignment in consignments:
        add_consigment_details(message, consignment)

def add_equipments(message : SegmentCollection, message_data : dict):
    equipments = message_data['equipments']
    for equipment in equipments:
        add_equipment(message, equipment)

# GRP5 A group of segments specifying the details of each consignment.
def add_consigment_details(message : SegmentCollection, consignment : dict):
    #CNI+1+DOCV373MOB909999'
    message.add_segment(Segment("CNI", consignment['cni_sequence_number'], consignment['cni_document_number'] + "-0")) # master bill number
    #RFF+BM:DOCV373MOB909999'
    message.add_segment(Segment("RFF", ["BM", consignment['cni_document_number']]))
    #CNT+7:55814:KGM'
    #CNT+8:60'
    message.add_segment(Segment("CNT", ["7", consignment['total_gross_weight'], "KGM"]))
    message.add_segment(Segment("CNT", ["8", consignment['number_of_pieces']])) # total pieces
    #LOC+9+CRMOB::139'
    #LOC+11+GBPME::139'
    #LOC+76+CRMOB::139'
    message.add_segment(Segment("LOC", "9", [consignment['departure_port'], None, "139"]))  #Place/port of loading
    message.add_segment(Segment("LOC", "11", [consignment['arrival_port'], None, "139"])) # Place/port of discharge
    message.add_segment(Segment("LOC", "76", [consignment['departure_port'], None, "139"])) # Original port of loading
    #GIS+23'
    message.add_segment(Segment("GIS", "23"))
    #NAD+SU+SUP1234+A PERSON, TEST ADDRESS, TOWN, POSTCODE'
    #NAD+CN+MOB00995+ANOTHER PERSON, A COMPANY, SOMEWHERE'
    #NAD+CZ+MOB00996+ANOTHER DIFFERENT PERSON, ANOTHER COMPANY, SOMEWHERE ELSE'
    message.add_segment(Segment("NAD", "SU", consignment['supplier']['id'], consignment['supplier']['name-address']))
    message.add_segment(Segment("NAD", "CN", consignment['consignee']['id'], consignment['consignee']['name-address'])) # receiver
    message.add_segment(Segment("NAD", "CZ", consignment['consignor']['id'], consignment['consignor']['name-address'])) # sender
    #GID+1+2880:UNT'
    message.add_segment(Segment("GID", "1", ["28880", "UNT"])) # num packages
    #FTX+AAA+++FREETEXT DESC, DETAILS'
    message.add_segment(Segment("FTX", "AAA", None, None, specified_values["goods"]))
    #MEA+AAE+G+KGM:55814'
    message.add_segment(Segment("MEA", "AAE", "G", ["KGM", consignment['total_gross_weight']]))
    #SGP+EQ123456+60'
    message.add_segment(Segment("SGP", consignment['equipment_identification_number'], consignment['number_of_pieces']))
    #PCI+24+SHIP1234'
    message.add_segment(Segment("PCI", "24", consignment['shipping_marks']))

def generate_random_location_gb(gb_ports):
    return random.choice(gb_ports)

def generate_random_location_world(ports):
    return random.choice(ports)

def initialise_port_codesets(codeset_dir):
    ports_filename = codeset_dir.joinpath("ports.dat")
    port_codes = []
    gb_port_codes = []
    with open(ports_filename, "rt") as textFile:
        for line in textFile.readlines():
            code = line.strip()
            port_codes.append(code)
            if line.startswith('GB'):
                gb_port_codes.append(code)
    return port_codes, gb_port_codes

def generate_equipment(equipment_number : str):
    equipment = {
        "identification_number" : f"EQ{random_string(size=8)}",
        "total_gross_weight" : "55814"
    }
    return equipment

def generate_consignment(consignment_number : str, equipment_identification_number : str):
    consignment = {
        "cni_sequence_number" : consignment_number,
        "supplier" : supplier,
        "consignee" : consignee,
        "consignor" : consignor,
        "cni_document_number" : f"DOC{random_string(size=12)}",
        "total_gross_weight" : "55814",
        "number_of_pieces" : "60",
        "shipping_marks" : f"SHPM{random_string(size=12)}",
        "departure_port" : specified_values["departure"],
        "arrival_port" : specified_values["arrival"],
        "equipment_identification_number" : equipment_identification_number
    }
    return consignment

def generate_equipments(number_of_equipments : int):
    equipments = []
    equipment_references = []
    for equipment_number in range(0, number_of_equipments):
        equipments.append(generate_equipment(str(equipment_number)))
        equipment_references.append(equipments[-1]['identification_number'])
    return equipments, equipment_references

def generate_consignments(number_of_consignments : int, equipment_ids : list):
    consigments = []
    for consignment_number in range(0, number_of_consignments):
        equipment_id = random.choice(equipment_ids)
        consigments.append(generate_consignment(str(consignment_number + 1), equipment_id))
    return consigments

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Generate a new CUSAR EDIFACT message')
    parser.add_argument('--consignor', metavar='consignor', nargs='?', type=str, help='use specified consignor (sender) identity rather than random')
    parser.add_argument('--consignee', metavar='consignee', nargs='?', type=str, help='use specified consignee (buyer) identity rather than random')
    parser.add_argument('--supplier', metavar='supplier', nargs='?', type=str, help='use specified supplier identity rather than random')
    parser.add_argument('--carrier', metavar='carrier', nargs='?', type=str, help='use specified carrier (Document/message issuer/sender) identity rather than random')
    parser.add_argument('--arrival', metavar='arrival', nargs='?', type=str, help='use specified arrival port code rather than random GB port')
    parser.add_argument('--departure', metavar='departure', nargs='?', type=str, help='use specified departure port code rather than random port')
    parser.add_argument('--consignments', metavar='consignments', nargs='?', type=int, default=1, help='Number of consignments to add')
    parser.add_argument('--equipments', metavar='equipments', nargs='?', type=int, default=1, help='Number of equipments to add')
    parser.add_argument('--goods', metavar='goods', nargs='?', type=str, help='Goods description')
    parser.add_argument('--vessel', metavar='vessel', nargs='?', type=str, help='Means of transport (vessel name)')
    parser.add_argument('--doser', action="store_true", default=False, help='Generate a template for data-doser')
    args = parser.parse_args()
    
    number_of_consignments = args.consignments
    number_of_equipments = args.equipments
    generate_data_doser_template = args.doser
    port_codes, gb_port_codes = initialise_port_codesets(Path('codelists'))
    specified_values = {}
    if args.consignee:
        specified_values["consignee"] = args.consignee
    else:
        specified_values["consignee"] = f"RECV{random_string(size=5)}"
    if args.consignor:
        specified_values["consignor"] = args.consignor
    else:
        specified_values["consignor"] = f"SEND{random_string(size=5)}"
    if args.supplier:
        specified_values["supplier"] = args.supplier
    else:
        specified_values["supplier"] = f"SUPP{random_string(size=5)}"
    if args.carrier:
        specified_values["carrier"] = args.carrier
    else:
        specified_values["carrier"] = f"CARRIER {random_string(size=8)}"
    if args.arrival:
        specified_values["arrival"] = args.arrival
    else:
         specified_values["arrival"] = generate_random_location_gb(gb_port_codes)
    if args.departure:
        specified_values["departure"] = args.departure
    else:
        specified_values["departure"] = generate_random_location_world(port_codes)
    if args.goods:
        FTX_STR_LEN = 70
        NUM_FTX_STRS = 5
        goods_input = args.goods[0:(FTX_STR_LEN*NUM_FTX_STRS)]
        specified_values["goods"]=[goods_input[y-FTX_STR_LEN:y] for y in range(FTX_STR_LEN, len(goods_input)+FTX_STR_LEN,FTX_STR_LEN)]
    else:
        specified_values["goods"] = ["good description"]
    if args.vessel:
        specified_values["means_of_transport"] = args.vessel
    else:
        specified_values["means_of_transport"] = f"TEST SHIP {random_string(size=10)}"

    now = datetime.now()
    arrival = now  + timedelta(days=30)

    supplier = {
        "id" : specified_values["supplier"],
        "name-address" : f"{specified_values['supplier']} PERSON, {specified_values['supplier']} COMPANY, SOMEWHERE"
    }

    consignee = {
        "id" : specified_values["consignee"],
        "name-address" : f"{specified_values['consignee']} PERSON, {specified_values['consignee']} COMPANY, SOMEWHERE"
    }

    consignor = {
        "id" : specified_values["consignor"],
        "name-address" : f"{specified_values['consignor']} PERSON, {specified_values['consignor']} COMPANY, SOMEWHERE"
    }

    equipment = {
        "identification_number" : f"EQ{random_string(size=8)}",
        "total_gross_weight" : "55814"
    }

    equipments, equipment_ids = generate_equipments(number_of_equipments)
    message_data = {
        "message_reference_number" : f"MREF{random_string(size=10)}",
        "sender_identification" : "SENDER",
        "recipient_identification" : "RECIPIENT",
        "send_date" : now.strftime("%y%m%d"),
        "send_time" : now.strftime("%H%M"),
        "interchangeControlReference" : f"ICR{random_string(size=10)}",
        "document_reference_number" : f"DOCREF{random_string(size=10)}",
        "submit_to_customs_timestamp" : now.strftime("%Y%m%d%H%M"),
        "sellers_message_reference_number" : f"SMREF{random_string(size=10)}",
        "conveyance_reference_number" : f"TRANS{random_string(size=10)}",
        "carrier_name" : specified_values['carrier'],
        "means_of_transport_identification" : random_string(size=8),
        "means_of_transport" : specified_values["means_of_transport"],
        "arrival_port" : specified_values["arrival"],
        "arrival_datetime_estimated" : arrival.strftime("%Y%m%d%H%M"),
        "arrival_datetime_scheduled" : arrival.strftime("%Y%m%d%H%M"),
        "equipments" : equipments,
        "consignments" : generate_consignments(number_of_consignments, equipment_ids)
    }

    if generate_data_doser_template:
        # use strings for the data-doser template variables so the generated edi can be used as a template
        message_data['message_reference_number'] = '$msg_ref'
        message_data['send_date'] = '$send_date'
        message_data['send_time'] = '$send_time'
        message_data['means_of_transport'] = '$ship'
        message_data['interchangeControlReference'] = '$src_number'
        message_data['message_reference_number'] = '$msg_ref'

    message = SegmentCollection()
    add_headers(message, message_data)
    add_cargo_report_sender_info(message, message_data)
    add_details_of_transport_and_arrival(message, message_data)
    add_general_indicator(message, message_data)
    add_equipments(message, message_data)
    add_consigments(message, message_data)
    add_footer(message, message_data)
    print(message.serialize())
