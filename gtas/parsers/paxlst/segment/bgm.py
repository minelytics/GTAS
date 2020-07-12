from gtas.parsers.paxlst.data_element_format import DataElementFormat
from gtas.parsers.paxlst.elements_structure import ElementsStructure


class BGM:
    def __init__(self, collections, group=None):
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements
        self.group = group

    @property
    def parse(self):
        if ElementsStructure(self.elements).struct == "list(str,str)":
            if self.group is None:
                y = [
                    ["C002:1001M", "an3", self.elements[0]],
                    ["C106:1004C", "an35", self.elements[1]],
                ]

                return {
                    "segment": self.tag,
                    "segment_description": "Beginning of Message",
                    "segment_function": "Beginning of Message",
                    "group": self.group,
                    "group_description": None,
                    "group_usage": None,
                    "level": 0,
                    "usage": "M",
                    "max_use": 1,
                    "purpose": "A segment to indicate the type and function of the message.",
                    "elements": DataElementFormat(y).process,
                }
