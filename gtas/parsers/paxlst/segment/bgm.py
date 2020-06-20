from gtas.parsers.paxlst.segment.base import Base


class BGM(Base):
    def document_name_code(self, val):
        switch = {
            "745": "PASSENGER_LIST",
            "250": "CREW_LIST",
            "266": "FLIGHT_STATUS_UPDATE",
            "336": "MASTER_CREW_LIST",
            "655": "GATE_PASS_REQUEST"
        }
        return switch.get(val, "BGM Unknown Document Name Code: " + val)

    def document_identifier(self, val):
        switch = {
            # PASSENGER_LIST
            "CP": "CHANGE_PAX_DATA",
            "XR": "CANCEL_RESERVATION",
            "RP": "REDUCTION_IN_PARTY",

            # FLIGHT_STATUS_UPDATE
            "CL": "FLIGHT_CLOSE",
            "CLNB": "FLIGHT_CLOSE_WITH_PAX_NOT_ON_BOARD",
            "CLOB": "FLIGHT_CLOSE_WITH_PAX_ON_BOARD",
            "XF": "CANCEL_FLIGHT",
            "CF": "CHANGE_FLIGHT",

            # CREW_LIST
            "C": "PASSENGER_FLIGHT_REGULAR_SCHEDULED_CREW",
            "CC": "PASSENGER_FLIGHT_CREW_CHANGE",
            "B": "CARGO_FLIGHT_REGULAR_SCHEDULED_CREW",
            "BC": "CARGO_FLIGHT_CREW_CHANGE",
            "A": "OVERFLIGHT_OF_PASSENGER_FLIGHT",
            "D": "OVERFLIGHT_OF_CARGO_FLIGHT",
            "E": "DOMESTIC_CONTINUANCE_OF_PASSENGER_FLIGHT_REGULAR_SCHEDULED_CREW",
            "EC": "DOMESTIC_CONTINUANCE_OF_PASSENGER_FLIGHT_CREW_CHANGE",
            "F": "DOMESTIC_CONTINUANCE_OF_CARGO_FLIGHT_REGULAR_SCHEDULED_CREW",
            "FC": "DOMESTIC_CONTINUANCE_OF_CARGO_FLIGHT_CREW_CHANGE",

            # MASTER_CREW_LIST
            "G": "ADD",
            "H": "DELETE",
            "I": "CHANGE"
        }
        return switch.get(val, "BGM Unknown Document Identifier: " + val)

    def process(self, data):
        sub_element = data.elements[0]
        key = self.document_name_code(sub_element)
        value = None

        if len(data.elements) == 1:
            value = "No Document Identifier used"
        elif len(data.elements) == 2:
            value = self.document_identifier(data.elements[1])

        return self.parsed_message(sub_element, key, value, data)
