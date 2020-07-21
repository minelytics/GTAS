from gtas.parsers.paxlst.element import Element


class DOC:
    def __init__(self, collections, group=None):
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements
        self.group = group

    @property
    def parse(self):
        if Element(self.elements).struct == "list(list(str,str,str),str)":
            if self.group == "Segment Group 5":
                y = [
                    ["C002:1001M", "an3", self.elements[0][0]],
                    ["C002:1131C", "an3", self.elements[0][1]],
                    ["C002:3055C", "an3", self.elements[0][2]],
                    ["C503:1004M", "an35", self.elements[1]],
                ]

                return {
                    "segment": self.tag,
                    "segment_description": "Document/Message Details",
                    "segment_function": "Traveler Document(s)",
                    "group": self.group,
                    "group_description": "Document/Message Details",
                    "group_usage": "C",
                    "level": 2,
                    "usage": "M",
                    "max_use": 1,
                    "purpose": "A segment identifying passenger and/or crew travel documents, such as passports, visas etc.",
                    "elements": Element(y).process,
                }
