class BASE:
    def tag(self, data):
        return data.tag


class LOC(BASE):
    def key(self, val):
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
            "100": "PLACE_OF_BIRTH"
        }
        return switch.get(val, "Not Identified")

    def process(self, data):
        return {
            'tag': data.tag,
            'element': {
                data.elements[0]: {
                    self.key(data.elements[0]): data.elements[1]
                }
            }
        }


class DTM(BASE):
    def key(self, val):
        switch = {
            "189": "DEPARTURE_DATETIME",
            "232": "ARRIVAL_DATETIME",
            "554": "DEPARTURE_ARRIVAL_DATETIME_MCL",
            "329": "DATE_OF_BIRTH",
            "36": "PASSPORT_EXPIRATION_DATE"
        }
        return switch.get(val, "Not Identified")

    def process(self, data):
        return data
