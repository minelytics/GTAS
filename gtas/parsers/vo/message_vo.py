from gtas.parsers.vo.flight_vo import FlightVo
from gtas.parsers.vo.bag_vo import BagVo


class MessageVo:
    def __init__(self, flights=None):
        self.__raw = None
        self.__hash_code = None
        self.__transmission_source = None
        self.__transmission_date = None
        self.__message_type = None
        self.__version = None

        if flights is None:
            self.__flights = []
        else:
            self.__flights = FlightVo(flights)

        self.__bag_vos = BagVo()

    def get_raw(self):
        return self.__raw

    def set_raw(self, raw):
        self.__raw = raw

    def get_hash_code(self):
        return self.__hash_code

    def set_hash_code(self, hash_code):
        self.__hash_code = hash_code

    def get_transmission_source(self):
        return self.__transmission_source

    def set_transmission_source(self, transmission_source):
        self.__transmission_source = transmission_source

    def get_transmission_date(self):
        return self.__transmission_date

    def set_transmission_date(self, transmission_date):
        self.__transmission_date = transmission_date

    def get_message_type(self):
        return self.__message_type

    def set_message_type(self, message_type):
        self.__message_type = message_type

    def get_version(self):
        return self.__version

    def set_version(self, version):
        self.__version = version

    def get_flights(self):
        return self.__flights

    def set_flights(self, flights):
        self.__flights = flights

    def get_bag_vos(self):
        return self.__bag_vos

    def set_bag_vos(self, bag_vos):
        self.__bag_vos = bag_vos

    def __str__(self):
        return """Raw: {}, Hash Code: {}, Transmission Source: {}, Transmission Date: {}, Message Type: {}, 
        Version: {}, Flights: {}, Bag Vos: {}""".format( self.__raw, self.__hash_code, self.__transmission_source,
                                                         self.__transmission_date, self.__message_type,
                                                         self.__version, self.__flights, self.__bag_vos)
