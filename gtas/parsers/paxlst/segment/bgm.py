from gtas.parsers.paxlst.data_element_format import DataElementFormat
from gtas.parsers.paxlst.elements_structure import ElementsStructure


class BGM:
    def __init__(self, segment_group, collections):
        self.segment_group = segment_group
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
                "segment_group": self.segment_group,
                "segment_tag": self.tag,
                "segment_elements": DataElementFormat(y).process,
            }
