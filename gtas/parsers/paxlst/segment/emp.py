from gtas.parsers.paxlst.element import Element


class EMP:
    def __init__(self, collections, group=None):
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements
        self.group = group

    @property
    def parse(self):
        if Element(self.elements).struct == "list(str,list(str,str,str))":
            if self.group == "Segment Group 4":
                y = [
                    ["9003M", "an1", self.elements[0]],
                    ["C948:9005M", "an3", self.elements[1][0]],
                    ["C948:1131C", "an3", self.elements[1][1]],
                    ["C948:3055C", "an3", self.elements[1][2]],
                ]

                return {
                    "segment": self.tag,
                    "segment_description": "Employment Details",
                    "segment_function": "Crew Member Status/Function",
                    "group": self.group,
                    "group_description": "Name and Address",
                    "group_usage": "C",
                    "level": 2,
                    "usage": "C",
                    "max_use": 1,
                    "purpose": "A segment to indicate the occupation of a passenger or the rank of crew.",
                    "elements": Element(y).process,
                }
