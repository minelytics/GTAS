from gtas.parsers.paxlst.data_element_format import DataElementFormat
from gtas.parsers.paxlst.elements_structure import ElementsStructure


class UNH:
    def __init__(self, segment_group, collections):
        self.segment_group = segment_group
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements

    @property
    def parse(self):
        if (
            ElementsStructure(self.elements).struct
            == "list(str,list(str,str,str,str,str),str,str)"
        ):
            y = [
                ["0062M", "an14", self.elements[0]],
                ["S009:0065M", "an6", self.elements[1][0]],
                ["S009:0052M", "an1", self.elements[1][1]],
                ["S009:0054M", "an3", self.elements[1][2]],
                ["S009:0051M", "an2", self.elements[1][3]],
                ["S009:0057C", "an4", self.elements[1][4]],
                ["0068C", "an35", self.elements[2]],
                ["S010:0070C", "an2", self.elements[3]],
                ["S010:0073C", "an1", None],
            ]

            return {
                "segment_group": self.segment_group,
                "segment_tag": self.tag,
                "segment_elements": DataElementFormat(y).process,
            }
