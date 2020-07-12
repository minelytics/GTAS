from gtas.parsers.paxlst.data_element_format import DataElementFormat
from gtas.parsers.paxlst.elements_structure import ElementsStructure


class BGM:
    def __init__(self, collections):
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements

    @property
    def parse(self):
        if ElementsStructure(self.elements).struct == "list(str,str)":
            y = [
                ["C002:1001M", "an3", self.elements[0]],
                ["C106:1004C", "an35", self.elements[1]],
            ]

            return {
                "segment": self.tag,
                "segment_description": "Beginning of Message",
                "group": None,
                "group_description": None,
                "level": 0,
                "usage": "Mandatory",
                "max_use": 1,
                "purpose": "A segment to indicate the type and function of the message.",
                "elements": DataElementFormat(y).process,
            }
