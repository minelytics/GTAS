from gtas.parsers.paxlst.data_element_format import DataElementFormat
from gtas.parsers.paxlst.elements_structure import ElementsStructure


class ATT:
    def __init__(self, collections, group=None):
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements
        self.group = group

    @property
    def parse(self):
        if ElementsStructure(self.elements).struct == "list(str,str,str)":
            if self.group == "Segment Group 4":
                y = [
                    ["9017M", "an1", self.elements[0]],
                    ["C956:9019M", "an1", self.elements[2]],
                ]

                return {
                    "segment": "ATT",
                    "segment_description": "Attribute",
                    "segment_function": "Traveler Gender",
                    "group": self.group,
                    "group_description": "Name and Address",
                    "group_usage": "C",
                    "level": 2,
                    "usage": "C",
                    "max_use": 1,
                    "purpose": "A segment specifying passenger's and/or crew attributes such as complexion and build.",
                    "elements": DataElementFormat(y).process,
                }
