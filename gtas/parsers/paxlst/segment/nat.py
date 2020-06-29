from gtas.parsers.paxlst.segment.base import Base


class NAT(Base):
    def process(self, data):
        sub_element = data.elements[0]
        key = "NATIONALITY_NAME_CODE"
        value = data.elements[1]

        return self.parsed_message(sub_element, key, value, data)
