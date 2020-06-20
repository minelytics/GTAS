from gtas.parsers.paxlst.segment.base import Base


class CNT(Base):
    def control_total_type_code_qualifier(self, val):
        switch = {
            "41": "TOTAL_PASSENGERS",
            "42": "TOTAL_CREW_MEMBERS"
        }
        return switch.get(val, "CNT Unknown Control Total Type Code Qualifier: " + val)

    def process(self, data):
        sub_element = key = value = None

        for element in data.elements:
            if isinstance(element, list):
                if len(element) == 2:
                    sub_element = element[0]
                    key = self.control_total_type_code_qualifier(sub_element)
                    value = element[1]

        return self.parsed_message(sub_element, key, value, data)
