from gtas.parsers.paxlst.element import Element


class FTX:
    def __init__(self, collections, group=None):
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements
        self.group = group

    @property
    def parse(self):
        if Element(self.elements).struct == "list(str,str,str,list(str,str))":
            if self.group == "Segment Group 4":
                y = [
                    ["4451M", "an3", self.elements[0]],
                    ["C108:4440M", "an80", self.elements[3][0]],
                    ["C108:4440M", "an80", self.elements[3][1]],
                ]

                return {
                    "segment": self.tag,
                    "segment_description": "Free Text",
                    "segment_function": "Bag Tag Identification Reporting",
                    "group": self.group,
                    "group_description": "Error Point Details",
                    "group_usage": "C",
                    "level": 2,
                    "usage": "C",
                    "max_use": 99,
                    "purpose": "A segment to provide explanation and/or supplementary information related to the specified application error.",
                    "elements": Element(y).process,
                }

        elif Element(self.elements).struct == "list(str,str,str,str)":
            if self.group == "Segment Group 4":
                y = [
                    ["4451M", "an3", self.elements[0]],
                    ["C108:4440M", "an80", self.elements[3]],
                ]

                return {
                    "segment": self.tag,
                    "segment_description": "Free Text",
                    "segment_function": "Bag Tag Identification Reporting",
                    "group": self.group,
                    "group_description": "Error Point Details",
                    "group_usage": "C",
                    "level": 2,
                    "usage": "C",
                    "max_use": 99,
                    "purpose": "A segment to provide explanation and/or supplementary information related to the specified application error.",
                    "elements": Element(y).process,
                }
