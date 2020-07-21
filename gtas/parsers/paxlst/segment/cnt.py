from gtas.parsers.paxlst.element import Element


class CNT:
    def __init__(self, collections, group=None):
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements
        self.group = group

    @property
    def parse(self):
        if Element(self.elements).struct == "list(list(str,str))":
            if self.group is None:
                y = [
                    ["C270:6069M", "an3", self.elements[0][0]],
                    ["C270:6066M", "n18", self.elements[0][1]],
                ]

                return {
                    "segment": self.tag,
                    "segment_description": "Control Total",
                    "segment_function": "Control Total",
                    "group": self.group,
                    "group_description": None,
                    "group_usage": None,
                    "level": 0,
                    "usage": "C",
                    "max_use": 1,
                    "purpose": "A segment specifying control totals such as the total number of passengers/ crew members in the message.",
                    "elements": Element(y).process,
                }
