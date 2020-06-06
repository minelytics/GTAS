from django.test import TestCase
from pydifact.message import Message
from gtas.parsers.vo.apis_message_vo import ApisMessageVo
from gtas.parsers.vo.flight_vo import FlightVo


class PaxlstParserUnedifactTest(TestCase):
    """Test for Paxlst Enedifact Parser"""

    def setUp(self):
        self.apis_message = "/apis-messages/apisMessage.txt"
        self.header = """UNA:+.? '
            UNB+UNOA:4+APIS*ABE+USADHS+070429:0900+000000001++USADHS'
            UNH+PAX001+PAXLST:D:05B:UN:IATA'
            BGM+745'"""
        self.trailer = """CNT+3:2'
            UNT+135+1'
            UNZ+1+020A07'"""

    def test_single_text_with_one_leg(self):
        apis = self.header + """TDT+20+UA123+++UA'
            LOC+125+YVR'
            DTM+189:0704291230:201'
            LOC+87+JFK'
            DTM+232:0704291600:201'""" + self.trailer

        flights = []

        for api in apis.split("\n"):
            collection = Message.from_str(api)

            for segment in collection.segments:
                if segment.tag.strip() == "LOC":

                    vo = ApisMessageVo(segment.elements)

                    if vo.get_flights().get_origin() is None:
                        pass
                    else:
                        flights.append(vo.get_flights().get_origin())

                    if vo.get_flights().get_destination() is None:
                        pass
                    else:
                        flights.append(vo.get_flights().get_destination())

        flight = FlightVo(flights)

        self.assertEqual("YVR", flight.get_origin())
        self.assertEqual("JFK", flight.get_destination())

    def tearDown(self):
        del self.apis_message
        del self.header
        del self.trailer
