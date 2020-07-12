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

        elif (
            ElementsStructure(self.elements).struct
            == "list(str,str,str,list(str,str),str,str,str,str,str)"
        ):
            y = [
                ["3035M", "an3", self.elements[0]],
                ["C080:3036C", "a35", self.elements[3][0]],
                ["C080:3036C", "a35", self.elements[3][1]],
                ["C059:3042C", "an35", self.elements[4]],
                ["3164C", "an35", self.elements[5]],
                ["C819:3229C", "an2", self.elements[6]],
                ["3251C", "an17", self.elements[7]],
                ["3207C", "an3", self.elements[8]],
            ]

            return {
                "segment": self.tag,
                "segment_description": "Name and Address",
                "segment_function": "Traveler Identification",
                "group": "Segment Group 4",
                "group_description": "Name and Address",
                "group_usage": "C",
                "level": 1,
                "usage": "M",
                "max_use": 1,
                "purpose": "A segment specifying name of the passenger or crew member.",
                "elements": DataElementFormat(y).process,
            }

        elif (
            ElementsStructure(self.elements).struct
            == "list(str,str,str,list(str,str,str),str,str,str,str,str)"
        ):
            y = [
                ["3035M", "an3", self.elements[0]],
                ["C080:3036C", "a35", self.elements[3][0]],
                ["C080:3036C", "a35", self.elements[3][1]],
                ["C080:3036C", "a35", self.elements[3][2]],
                ["C059:3042C", "an35", self.elements[4]],
                ["3164C", "an35", self.elements[5]],
                ["C819:3229C", "an2", self.elements[6]],
                ["3251C", "an17", self.elements[7]],
                ["3207C", "an3", self.elements[8]],
            ]

            return {
                "segment": self.tag,
                "segment_description": "Name and Address",
                "segment_function": "Traveler Identification",
                "group": "Segment Group 4",
                "group_description": "Name and Address",
                "group_usage": "C",
                "level": 1,
                "usage": "M",
                "max_use": 1,
                "purpose": "A segment specifying name of the passenger or crew member.",
                "elements": DataElementFormat(y).process,
            }
