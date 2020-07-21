from gtas.parsers.paxlst.element import Element


class NAT:
    def __init__(self, collections, group=None):
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements
        self.group = group

    @property
    def parse(self):
        if Element(self.elements).struct == "list(str,str)":
            if self.group == "Segment Group 4":
                y = [
                    ["3493M", "an1", self.elements[0]],
                    ["C042:3293M", "an3", self.elements[1]],
                ]

                return {
                    "segment": self.tag,
                    "segment_description": "Nationality",
                    "segment_function": "Traveler Citizenship",
                    "group": self.group,
                    "group_description": "Name and Address",
                    "group_usage": "C",
                    "level": 2,
                    "usage": "C",
                    "max_use": 1,
                    "purpose": "A segment to indicate the nationality of a passenger and/or crew.",
                    "elements": Element(y).process,
                }
