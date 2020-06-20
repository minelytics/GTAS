from gtas.parsers.paxlst.segment.base import Base


class DOC(Base):
    def code_list_identification_code(self, val):
        switch = {
            "P": "PASSPORT",
            "C": "PERMANENT_RESIDENT_CARD",
            "A": "RESIDENT_ALIEN_CARD",
            "M": "US_MILITARY_ID",
            "T": "RE-ENTRY_OR_REFUGEE_PERMIT",
            "IN": "NEXUS_CARD",
            "IS": "SENTRI_CARD",
            "F": "FACILITATION_CARD",
            "L": "PILOTS_LICENSE"
        }
        return switch.get(val, "DOC Unknown Code List Identification Code: " + val)

    def process(self, data):
        temp = {"tag": "DOC", "element": {}}

        if isinstance(data.elements[0], list):
            sub_element = data.elements[0][0]
            key = self.code_list_identification_code(sub_element)
            value = data.elements[1]

            temp["element"].update({sub_element: {key: value}})
            temp["element"][sub_element].update({"IDENTIFICATION_CODE": "US_DHS_SPECIAL_CODES"})
            temp["element"][sub_element].update({"RESPONSIBLE_AGENCY_CODE": "US_DEPARTMENT_OF_HOMELAND_SECURITY"})
        else:
            sub_element = data.elements[0]
            key = self.code_list_identification_code(sub_element)
            value = data.elements[1]

            return self.parsed_message(sub_element, key, value, data)
        return temp
