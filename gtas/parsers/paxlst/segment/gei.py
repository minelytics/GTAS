from gtas.parsers.paxlst.data_element_format import DataElementFormat
from gtas.parsers.paxlst.elements_structure import ElementsStructure


class GEI:
    def __init__(self, collections, group=None):
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements
        self.group = group

    @property
    def parse(self):
        if ElementsStructure(self.elements).struct == "list(str,str)":
            if self.group == "Segment Group 4":
                y = [
                    ["9649M", "an3", self.elements[0]],
                    ["C012:7365M", "an3", self.elements[1]],
                ]

                return {
                    "segment": self.tag,
                    "segment_description": "Processing Information",
                    "segment_function": "Verification Indicator",
                    "group": self.group,
                    "group_description": "Name and Address",
                    "group_usage": "C",
                    "level": 2,
                    "usage": "C",
                    "max_use": 2,
                    "purpose": "A segment to specify indicators such as risk assessment.",
                    "elements": DataElementFormat(y).process,
                }
