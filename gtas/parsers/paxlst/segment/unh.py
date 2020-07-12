from gtas.parsers.paxlst.data_element_format import DataElementFormat


class UNH:
    def __init__(self, segment_group, elements):
        self.segment_group = segment_group
        self.elements = elements

    @property
    def parse(self):
        if len(self.elements.segments[0].elements) == 4:
            y = [
                ["0062M", "an14", self.elements.segments[0].elements[0]],
                ["S009:0065M", "an6", self.elements.segments[0].elements[1][0]],
                ["S009:0052M", "an1", self.elements.segments[0].elements[1][1]],
                ["S009:0054M", "an3", self.elements.segments[0].elements[1][2]],
                ["S009:0051M", "an2", self.elements.segments[0].elements[1][3]],
                ["S009:0057C", "an4", self.elements.segments[0].elements[1][4]],
                ["0068C", "an35", self.elements.segments[0].elements[2]],
                ["S010:0070C", "an2", self.elements.segments[0].elements[3]],
                ["S010:0073C", "an1", None],
            ]

            return {
                "segment_group": self.segment_group,
                "segment_tag": self.elements.segments[0].tag,
                "segment_elements": DataElementFormat(y).process,
            }
