from gtas.parsers.paxlst.data_element_format import DataElementFormat
from gtas.parsers.paxlst.elements_structure import ElementsStructure


class DTM:
    def __init__(self, collections):
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements

    @property
    def parse(self):
        if ElementsStructure(self.elements).struct == "list(list(str,str,str))":
            y = [
                ["C507:2005M", "an3", self.elements[0][0]],
                ["C507:2380M", "n10", self.elements[0][1]],
                ["C507:2379C", "an3", self.elements[0][2]],
            ]

            return {
                "segment": self.tag,
                "segment_description": "Date/Time/Period",
                "group": "Segment Group 3",
                "group_description": "Place/Location Identification",
                "group_usage": "C",
                "level": 3,
                "usage": "C",
                "max_use": 1,
                "purpose": "A segment to specify associated dates and/or times as required related to locations.",
                "elements": DataElementFormat(y).process,
            }
