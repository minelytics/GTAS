from gtas.parsers.paxlst.segment.base import Base

class ATT(Base):
    def attribute_function_code_qualifier(self, val):
        switch = {
            "2": "GENDER"
        }
        return switch.get(val, "ATT Unknown Attribute Function Code Qualifier: " + val)

    def process(self, data):
        sub_element = data.elements[0]
        key = self.attribute_function_code_qualifier(sub_element)
        value = data.elements[2]

        return self.parsed_message(sub_element, key, value, data)
