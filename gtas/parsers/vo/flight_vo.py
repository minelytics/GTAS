import uuid


class FlightVo:
    def __init__(self, __elements=None):
        self.__uuid = uuid.uuid4()
        self.__is_marketing_flight = False
        self.__flight_number = None
        self.__origin = None
        self.__destination = None

        if __elements is None:
            self.__elements = []
            self.__origin = ""
            self.__destination = ""
        else:
            self.__elements = __elements

            if self.__elements[0] == '125':
                self.__origin = self.__elements[1]
            elif self.__elements[0] == '87':
                self.__destination = self.__elements[1]
            else:
                self.__origin = self.__elements[0]
                self.__destination = self.__elements[1]

    def set_uuid(self, __uuid):
        self.__uuid = __uuid

    def get_uuid(self):
        return self.__uuid

    def is_marketing_flight(self):
        return self.__is_marketing_flight

    def set_markerting_flight(self, is_marketing_flight):
        self.__is_marketing_flight = is_marketing_flight

    def get_flight_number(self):
        return self.__flight_number

    def set_flight_number(self, flight_number):
        self.__flight_number = flight_number

    def get_origin(self):
        return self.__origin

    def set_origin(self, origin):
        self.__origin = origin

    def get_destination(self):
        return self.__destination

    def set_destination(self, destination):
        self.__destination = destination

    def __str__(self):
        return """UUID: {}, Is Marketing Flight: {}, Flight Number: {}, Origin: {}, Destination: {}""".format(
            self.__uuid,
            self.__is_marketing_flight,
            self.__flight_number,
            self.__origin,
            self.__destination)
