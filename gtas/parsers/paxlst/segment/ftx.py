from gtas.parsers.paxlst.data_element_format import DataElementFormat
from gtas.parsers.paxlst.elements_structure import ElementsStructure


class FTX:
    def __init__(self, collections):
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements

    @property
    def parse(self):
        if ElementsStructure(self.elements).struct == "list(str,str,str,list(str,str))":
            y = [
                ["4451M", "an3", self.elements[0]],
                ["C108:4440M", "an80", self.elements[3][0]],
                ["C108:4440M", "an80", self.elements[3][1]],
            ]

            return {
                "segment": self.tag,
                "segment_description": "Free Text",
                "segment_function": "Bag Tag Identification Reporting",
                "group": "Segment Group 4",
                "group_description": "Error Point Details",
                "group_usage": "C",
                "level": 2,
                "usage": "C",
                "max_use": 99,
                "purpose": "A segment to provide explanation and/or supplementary information related to the specified application error.",
                "elements": DataElementFormat(y).process,
            }

        elif ElementsStructure(self.elements).struct == "list(str,str,str,str)":
            y = [
                ["4451M", "an3", self.elements[0]],
                ["C108:4440M", "an80", self.elements[3]],
            ]

            return {
                "segment": self.tag,
                "segment_description": "Free Text",
                "segment_function": "Bag Tag Identification Reporting",
                "group": "Segment Group 4",
                "group_description": "Error Point Details",
                "group_usage": "C",
                "level": 2,
                "usage": "C",
                "max_use": 99,
                "purpose": "A segment to provide explanation and/or supplementary information related to the specified application error.",
                "elements": DataElementFormat(y).process,
            }
