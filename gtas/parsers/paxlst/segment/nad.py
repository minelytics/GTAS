from gtas.parsers.paxlst.data_element_format import DataElementFormat
from gtas.parsers.paxlst.elements_structure import ElementsStructure


class NAD:
    def __init__(self, collections):
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements

    @property
    def parse(self):
        if ElementsStructure(self.elements).struct == "list(str,str,str,str)":
            y = [
                ["3035M", "an2", self.elements[0]],
                ["C080:3036M", "an35", self.elements[3]],
            ]

            return {
                "segment": self.tag,
                "segment_description": "Name and Address",
                "segment_function": "Reporting Party",
                "group": "Segment Group 1",
                "group_description": "Name and Address",
                "group_usage": "C",
                "level": 1,
                "usage": "M",
                "max_use": 1,
                "purpose": "A segment to identify the name, address and related function.",
                "elements": DataElementFormat(y).process,
            }
