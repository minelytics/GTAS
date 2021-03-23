__author__ = "Chris Humphreys"
__version__ = "1.0.0"
__license__ = "GPL3"

import edifact
import string
import random
import json
from pathlib import Path



class GenerateHandler(edifact.Handler):

    def visit_codeset_element(self, data_element_schema, element, codeset_manager, codeset_code, verbose):
        #leave untouched for now
        return False, element

    def visit_literal_element(self, data_element_schema, element, codeset_manager):
        code = data_element_schema['code']
        if code in self._all_pii_attributes:
            requested_generator = self._all_pii_attributes[code]['generator']
            if requested_generator in self.generators:
                new_value = self.generators[requested_generator](data_element_schema, element, codeset_manager)
                return True, new_value
            else:
                raise Exception("Unknown generator {}".format(requested_generator))
        return False, element

    def visit_segment(self, segment, schema, schema_position):
        #print("Entering segment:{}".format(segment.tag))
        self._current_segment = segment
        
    def visit_unknown_segment(self, segment):
        #Stop if we don't understand the message - can't be sure there isn't PII in there
        msg = 'Unknown Segment tag: {}, content: {}'.format(segment.tag, segment.elements)
        raise Exception(msg)

    def start(self):
        pass

    def end(self):
        pass
    
    # ----------------------------------------------------------------------------------------------

    generators = {}
    generated_value_store = {}
    ports = []
    gb_ports = []
    LOCATION_SEGMENT_TAG = "LOC"
    NAME_ADDRESS_SEGMENT_TAG = "NAD"
    LOCATION_FUNCTION_CODESET = "3227"
    ARRIVAL_LOCATION = "60" # Codeset 3227 Arrival location value
    PARTY_QUALIFIER_CODESET = "3035"
    CONSIGNOR_CODE = "CZ" # Codeset 3035 Consignor (sender) party qualifier value
    CONSIGNEE_CODE = "CN" # Codeset 3035 Consignee (receiver) party qualifier value
    SUPPLIER_CODE = "SU" # Codeset 3035 Supplier party qualifier value
    CARRIER_CODE = "MS"  # Codeset 3035 Document/message issuer/sender (Carrier) party qualifier value
    # Pre-specified identities - use these instead of generating random identities, ueful for building transaction history
    _specified_identities = {}
    # Pre-specified locations - use these instead of generating random locations
    _specified_locations = {}  

    def random(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    def length_for_random(self, data_element_schema):
        max_length = data_element_schema["content_length"]
        if '..' in max_length:
            max_length = max_length.split('..')[1]
        return int(max_length)

    def generator_random(self, data_element_schema, element, codeset_manager):
        return self.random(self.length_for_random(data_element_schema))

    def generate_random_location_gb(self):
        return random.choice(self.gb_ports)

    def generate_random_location_world(self):
        return random.choice(self.ports)

    # Choose a random port form the pre-loaded port list
    # attempt to use the location_function_code from the same segment
    # if it looks like arrival - select a random GB port
    # if it is something else - select a random worldwide port
    def generator_random_location(self, data_element_schema, element, codeset_manager):
        port = None
        location_type = self.loc_location_function_code()
        if location_type in self._specified_locations:
            port = self._specified_locations[location_type]
        else:    
            if self.is_arrival_location(location_type):
                port = self.generate_random_location_gb()
            else:
                port = self.generate_random_location_world()
        
        location_type_desc = codeset_manager.codeset_lookup(location_type, self.LOCATION_FUNCTION_CODESET)["name"]
        print("Port({}):{}".format(location_type_desc, port))
        return port

    def is_arrival_location(self, location_type):
        return self.ARRIVAL_LOCATION == location_type

    def loc_location_function_code(self):
        if self._current_segment != None:
            if self._current_segment.tag == self.LOCATION_SEGMENT_TAG:
                return self._current_segment.elements[0]
        return None

    # Generate a random identification reference
    # Attempt to use the associated party qualifier to prefix the code
    # with either: "SU" for supplier, "CN" for consignee (buyer), "CZ" for consignor (sender) so 
    # we can read who is who in the obfuscated data
    def generator_random_identification(self, data_element_schema, element, codeset_manager):
        party = self.nad_party_qualifier()
        party_identification = None
        if party in self._specified_identities:
            party_identification = self._specified_identities[party]
        else:
            party_identification = self.nad_party_qualifier() + self.random(15)
        
        party_desc = codeset_manager.codeset_lookup(party, self.PARTY_QUALIFIER_CODESET)["name"]
        print("Party({}):{}".format(party_desc, party_identification))
        return party_identification

    # Attempt to determine the qualifier
    def nad_party_qualifier(self):
        if self._current_segment != None:
            if self._current_segment.tag == self.NAME_ADDRESS_SEGMENT_TAG:
                return self._current_segment.elements[0]
        return "UNK"


    def generator_random_addressline(self, data_element_schema, element, codeset_manager):
        return self.random(10) + "ADDR, TOWN, POSTCODE"

    def generator_random_city(self, data_element_schema, element, codeset_manager):
        return self.random(10) + "CITY"

    def generator_random_transport(self, data_element_schema, element, codeset_manager):
        self._transport_name = self.random(8) + " SHIP"
        print("Vessel name: {}".format(self._transport_name))
        return self._transport_name

    # Generate a randome value and store it under the element descriptor
    # useful for message references which are global and used in multiple places
    # in the message 
    def generator_random_and_store(self, data_element_schema, element, codeset_manager):
        if data_element_schema["code"] not in self.generated_value_store:
            new_value = self.random(self.length_for_random(data_element_schema))
            self.generated_value_store[data_element_schema["code"]] = new_value
        return self.generated_value_store[data_element_schema["code"]]

    def generator_random_date_time_past(self, data_element_schema, element, codeset_manager):
        # TODO Fix me. Need to check 2379 Date/time/period format qualifier
        return element


    def initialise_generators(self):
        self.generators = {
            'random' : self.generator_random,
            'random_and_store' : self.generator_random_and_store,
            'random_location' : self.generator_random_location,
            'random_identification' : self.generator_random_identification,
            'random_address_line' : self.generator_random_addressline,
            'random_transport' : self.generator_random_transport,
            'date_time_past' : self.generator_random_date_time_past,
            'random_city' : self.generator_random_city
        }   

    def initialise_codesets(self):
        codeset_dir = Path("codelists")
        self.ports, self.gb_ports = self.initialise_port_codesets(codeset_dir)

    def initialise_port_codesets(self, codeset_dir):
        ports_filename = codeset_dir.joinpath("ports.dat")
        port_codes = []
        gb_port_codes = []
        with open(ports_filename, "rt") as textFile:
            for line in textFile.readlines():
                code = line.strip()
                port_codes.append(code)
                if line.startswith('GB'):
                    gb_port_codes.append(code)
        #print("Read {} port codes".format(len(port_codes)))
        return port_codes, gb_port_codes

    def initialise(self, specified_values):
        self.initialise_generators()
        self.initialise_codesets()
        self.initialise_identities(specified_values)
        self.initialise_locations(specified_values)
        self.initialise_pii()

    def initialise_pii(self):
        self._all_pii_attributes = {}
        with open("pii.json") as json_file:
            pii = json.load(json_file)
        for segment in pii:
            for attribute in pii[segment]:
                attribute['segment'] = segment
                code = attribute['code']
                self._all_pii_attributes[code] = attribute


    def initialise_identities(self, specified_values):
        if "consignor" in specified_values:
            self._specified_identities[self.CONSIGNOR_CODE] = specified_values["consignor"]
        if "consignee" in specified_values:
            self._specified_identities[self.CONSIGNEE_CODE] = specified_values["consignee"]
        if "supplier" in specified_values:
            self._specified_identities[self.SUPPLIER_CODE] = specified_values["supplier"]
        if "carrier" in specified_values:
            self._specified_identities[self.CARRIER_CODE] = specified_values["carrier"]
    
    def initialise_locations(self, specified_values):
        if "arrival" in specified_values:
            self._specified_locations[self.ARRIVAL_LOCATION] = specified_values["arrival"]