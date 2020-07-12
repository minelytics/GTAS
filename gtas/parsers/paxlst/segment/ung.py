from gtas.parsers.paxlst.data_element_format import DataElementFormat


class UNG:
    def __init__(self, segment_group, elements):
        self.segment_group = segment_group
        self.elements = elements

    @property
    def parse(self):
        y = [
            ["0038M", "an6", self.elements.segments[0].elements[0]],
            ["S006:0040M", "an35", self.elements.segments[0].elements[1]],
            ["S007:0044M", "an35", self.elements.segments[0].elements[2]],
            ["S004:0017M", "n6", self.elements.segments[0].elements[3][0]],
            ["S004:0019M", "n4", self.elements.segments[0].elements[3][1]],
            ["0048M", "an14", self.elements.segments[0].elements[4]],
            ["0051M", "an2", self.elements.segments[0].elements[5]],
            ["S008:0052M", "an1", self.elements.segments[0].elements[6][0]],
            ["S008:0054M", "an3", self.elements.segments[0].elements[6][1]],
        ]

        return {
            "segment_group": self.segment_group,
            "segment_tag": self.elements.segments[0].tag,
            "segment_elements": DataElementFormat(y).process,
        }
