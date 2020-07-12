from gtas.parsers.paxlst.data_element_format import DataElementFormat
from gtas.parsers.paxlst.elements_structure import ElementsStructure


class LOC:
    def __init__(self, collections):
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements

    @property
    def parse(self):
        if ElementsStructure(self.elements).struct == "list(str,str)":
            y = [
                ["3227M", "n3", self.elements[0]],
                ["C517:3225M", "an3", self.elements[1]],
            ]

            return {
                "segment": self.tag,
                "segment_description": "Place/Location Identification",
                "group": "Segment Group 3",
                "group_description": "Place/Location Identification",
                "group_usage": "C",
                "level": 2,
                "usage": "M",
                "max_use": 1,
                "purpose": "A segment to specify locations such as place of departure, place of destination, country of ultimate destination, country and/or place of transit, country of transit termination, etc. of a passenger/crew.",
                "elements": DataElementFormat(y).process,
            }
