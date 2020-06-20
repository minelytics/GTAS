from gtas.parsers.paxlst.segment.base import Base


class COM(Base):
    def communication_address_code_qualifier(self, val):
        switch = {
            "TE": "TELEPHONE",
            "FX": "TELEFAX",
            "EM": "EMAIL"
        }
        return switch.get(val, "COM Unknown Communication Address Code Qualifier: " + val)

    def process(self, data):
        temp = {"tag": "COM", "element": {}}
        for element in data.elements:
            if isinstance(element, list):
                sub_element = element[1]
                key = self.communication_address_code_qualifier(sub_element)
                value = element[0]

                if len(data.elements) == 1:
                    return self.parsed_message(sub_element, key, value, data)
                elif len(data.elements) > 1:
                    temp["element"].update({sub_element: {key: value}})
        return temp
