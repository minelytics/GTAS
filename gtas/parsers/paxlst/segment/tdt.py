from gtas.parsers.paxlst.element import Element


class TDT:
    def __init__(self, collections, group=None):
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements
        self.group = group

    @property
    def parse(self):
        if Element(self.elements).struct == "list(str,str,str,str,str)":
            if self.group == "Segment Group 2":
                y = [
                    ["8051M", "an3", self.elements[0]],
                    ["8028C", "an8", self.elements[1]],
                    ["C040:3127C", "an17", self.elements[4]],
                ]

                return {
                    "segment": self.tag,
                    "segment_description": "Transport Information",
                    "segment_function": "Flight Identification",
                    "group": self.group,
                    "group_description": "Transport Information",
                    "group_usage": "M",
                    "level": 1,
                    "usage": "M",
                    "max_use": 10,
                    "purpose": "A segment to specify details of transport related to each leg, including means of transport, mode of transport name and/or number of vessel and/or vehicle and/or flight.",
                    "elements": Element(y).process,
                }
