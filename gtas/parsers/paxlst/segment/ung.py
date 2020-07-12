from gtas.parsers.paxlst.data_element_format import DataElementFormat
from gtas.parsers.paxlst.elements_structure import ElementsStructure


class UNG:
    def __init__(self, collections):
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements

    @property
    def parse(self):
        if (
            ElementsStructure(self.elements).struct
            == "list(str,str,str,list(str,str),str,str,list(str,str))"
        ):
            y = [
                ["0038M", "an6", self.elements[0]],
                ["S006:0040M", "an35", self.elements[1]],
                ["S007:0044M", "an35", self.elements[2]],
                ["S004:0017M", "n6", self.elements[3][0]],
                ["S004:0019M", "n4", self.elements[3][1]],
                ["0048M", "an14", self.elements[4]],
                ["0051M", "an2", self.elements[5]],
                ["S008:0052M", "an1", self.elements[6][0]],
                ["S008:0054M", "an3", self.elements[6][1]],
            ]

            return {
                "segment": self.tag,
                "segment_description": "Functional Group Header",
                "group": None,
                "group_description": None,
                "level": 0,
                "usage": "Conditional",
                "max_use": 1,
                "purpose": "To begin a group of like transaction. Only one grouping of transactions will be allowed for this implementation.",
                "elements": DataElementFormat(y).process,
            }
