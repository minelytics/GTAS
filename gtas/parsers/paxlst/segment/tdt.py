from gtas.parsers.paxlst.segment.base import Base


class TDT(Base):
    def transport_stage_qualifier(self, val):
        switch = {
            "20": "ARRIVING_OR_DEPARTING_FLIGHT",
            "34": "OVER_FLIGHT"
        }
        return switch.get(val, "TDT Unkown Transport Stage Qualifier: " + val)

    def process(self, data):
        sub_element = data.elements[0]
        key = self.transport_stage_qualifier(sub_element)
        value = data.elements[1]

        temp = {"tag": "TDT", "element": {sub_element:{key:value}}}
        if len(data.elements) == 5:
            temp["element"].update({"CARRIER_IDENTIFIER": "UA"})
        else:
            return self.parsed_message(sub_element, key, value, data)

        return temp