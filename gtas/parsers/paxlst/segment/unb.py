from gtas.parsers.paxlst.data_element_format import DataElementFormat
from gtas.parsers.paxlst.elements_structure import ElementsStructure


class UNB:
    def __init__(self, collections, group=None):
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements
        self.group = group

    @property
    def parse(self):
        if (
            ElementsStructure(self.elements).struct
            == "list(list(str,str),str,str,list(str,str),str,str,str)"
        ):
            if self.group is None:
                y = [
                    ["S001:0001M", "a4", self.elements[0][0]],
                    ["S001:0002M", "an1", self.elements[0][1]],
                    ["S002:0004M", "an35", self.elements[1]],
                    ["S002:0007C", "an2", "ZZ"],
                    ["S003:0010M", "an35", self.elements[2]],
                    ["S003:0007C", "an2", "ZZ"],
                    ["S004:0017M", "n6", self.elements[3][0]],
                    ["S004:0019M", "n4", self.elements[3][1]],
                    ["0020M", "an14", self.elements[4]],
                    ["0026M", "an14", self.elements[6]],
                ]

                return {
                    "segment": self.tag,
                    "segment_description": "Interchange Header",
                    "segment_function": "Interchange Header",
                    "group": self.group,
                    "group_description": None,
                    "group_usage": None,
                    "level": 0,
                    "usage": "M",
                    "max_use": 1,
                    "purpose": "To start, identify and specify an interchange",
                    "elements": DataElementFormat(y).process,
                }
