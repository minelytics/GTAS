from gtas.parsers.paxlst.data_element_format import DataElementFormat


class UNB:
    def __init__(self, segment_group, elements):
        self.segment_group = segment_group
        self.elements = elements

    @property
    def parse(self):
        y = [
            ["S001:0001M", "a4", self.elements.segments[0].elements[0][0]],
            ["S001:0002M", "an1", self.elements.segments[0].elements[0][1]],
            ["S002:0004M", "an35", self.elements.segments[0].elements[1]],
            ["S002:0007C", "an2", "ZZ"],
            ["S003:0010M", "an35", self.elements.segments[0].elements[2]],
            ["S003:0007C", "an2", "ZZ"],
            ["S004:0017M", "n6", self.elements.segments[0].elements[3][0]],
            ["S004:0019M", "n4", self.elements.segments[0].elements[3][1]],
            ["0020M", "an14", self.elements.segments[0].elements[4]],
            ["0026M", "an14", self.elements.segments[0].elements[6]],
        ]

        return {
            "segment_group": self.segment_group,
            "segment_tag": self.elements.segments[0].tag,
            "segment_elements": DataElementFormat(y).process,
        }
