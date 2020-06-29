from gtas.parsers.paxlst.segment.base import Base


class NAD(Base):
    def party_function_code_qualifier(self, val):
        switch = {
            "MS": "REPORTING_PARTY",
            "FL": "PASSENGER",
            "FM": "CREW_MEMBER",
            "DDU": "INTRANSIT_PASSENGER",
            "DDT": "INTRANSIT_CREW_MEMBER"
        }
        return switch.get(val, "NAD Unkown Party Function Code Qualifier: " + val)

    def name(self, data):
        if isinstance(data.elements[3], str):
            return data.elements[3]
        elif isinstance(data.elements[3], list):
            if len(data.elements[3]) == 2:
                return " ".join([data.elements[3][1], data.elements[3][0]])
            elif len(data.elements[3]) == 3:
                return " ".join([data.elements[3][1], data.elements[3][2], data.elements[3][0]])

    def process(self, data):
        sub_element = data.elements[0]
        key = self.party_function_code_qualifier(sub_element)
        value = self.name(data)

        temp = {"tag": "NAD", "element": {sub_element:{key:value}}}
        if len(data.elements) == 9:
            temp["element"].update({
                "ADDRESS":{
                    "NAME_AND_STREET_IDENTIFIER": data.elements[4],
                    "CITY": data.elements[5],
                    "COUNTRY_SUB_CODE": data.elements[6],
                    "POSTAL_CODE": data.elements[7],
                    "COUNTRY_CODE": data.elements[8]
                }
            })
        else:
            return self.parsed_message(sub_element, key, value, data)

        return temp