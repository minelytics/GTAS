from gtas.parsers.paxlst.data_element_format import DataElementFormat
from gtas.parsers.paxlst.elements_structure import ElementsStructure


class COM:
    def __init__(self, collections, group=None):
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements
        self.group = group

    @property
    def parse(self):
        if (
            ElementsStructure(self.elements).struct
            == "list(list(str,str),list(str,str))"
        ):
            if self.group == "Segment Group 1":
                y = [
                    ["C076:3148M", "an20", self.elements[0][0]],
                    ["C076:3155M", "an3", self.elements[0][1]],
                    ["C076:3148C", "an20", self.elements[1][0]],
                    ["C076:3155C", "an3", self.elements[1][1]],
                ]

                return {
                    "segment": self.tag,
                    "segment_description": "Communication Contact",
                    "segment_function": "Reporting Party Contact Information",
                    "group": self.group,
                    "group_description": "Name and Address",
                    "group_usage": "C",
                    "level": 2,
                    "usage": "C",
                    "max_use": 1,
                    "purpose": "A segment to identify communication numbers of departments or persons to whom communication should be directed (e.g., telephone, fax number).",
                    "elements": DataElementFormat(y).process,
                }
