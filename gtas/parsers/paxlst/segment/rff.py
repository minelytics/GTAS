from gtas.parsers.paxlst.segment.base import Base


class RFF(Base):
    def reference_code_qualifier(self, val):
        switch = {
            "TN": "TRANSACTION_REFERENCE_NUMBER",
            "AVF": "PASSENGER_RESERVATION_NUMBER",
            "ABO": "AIRCRAFT_OPERATOR_UNIQUE_PASSENGER_REFERENCE_IDENTIFIER",
            "SEA": "SEAT_NUMBER",
            "AEA": "GOVERNMENT_AGENCY_REFERENCE_NUMBER",
            "CR": "CUSTOMER_REFERENCE_NUMBER"
        }
        return switch.get(val, "RFF Unkown Reference Code Qualifier: " + val)

    def process(self, data):
        sub_element = data.elements[0][0]
        key = self.reference_code_qualifier(sub_element)
        value = data.elements[0][1]

        return self.parsed_message(sub_element, key, value, data)
