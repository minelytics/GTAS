from gtas.parsers.paxlst.segment.base import Base


class LOC(Base):
    def location_function_code_qualifier(self, val):
        switch = {
            "125": "DEPARTURE_AIRPORT",
            "87": "ARRIVAL_AIRPORT",
            "92": "BOTH_DEPARTURE_AND_ARRIVAL_AIRPORT",
            "130": "FINAL_DESTINATION",
            "188": "FILING_LOCATION",
            "172": "REPORTING_LOCATION",
            "91": "GATE_PASS_ISSUE_LOCATION",
            "22": "AIRPORT_OF_FIRST_US_ARRIVAL",
            "174": "COUNTRY_OF_RESIDENCE",
            "178": "PORT_OF_EMBARKATION",
            "179": "PORT_OF_DEBARKATION",
            "180": "PLACE_OF_BIRTH"
        }
        return switch.get(val, "LOC Unknown Location Function Code Qualifier: " + val)

    def process(self, data):
        sub_element = data.elements[0]
        key = self.location_function_code_qualifier(data.elements[0])
        value = data.elements[1]

        return self.parsed_message(sub_element, key, value, data)
