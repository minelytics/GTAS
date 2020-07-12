from gtas.parsers.paxlst.data_element_format import DataElementFormat
from gtas.parsers.paxlst.elements_structure import ElementsStructure


class RFF:
    def __init__(self, segment_group, collections):
        self.segment_group = segment_group
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements

    @property
    def parse(self):
        if ElementsStructure(self.elements).struct == "list(list(str,str,str,str,str))":
            y = [
                ["C506:1153M", "an3", self.elements[0][0]],
                ["C506:1154M", "an25", self.elements[0][1]],
                ["C506:1060C", "an3", self.elements[0][4]],
            ]

            return {
                "segment_group": self.segment_group,
                "segment_tag": self.tag,
                "segment_elements": DataElementFormat(y).process,
            }
