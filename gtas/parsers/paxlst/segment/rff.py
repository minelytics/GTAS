from gtas.parsers.paxlst.data_element_format import DataElementFormat


class RFF:
    def __init__(self, collections, group=None):
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements
        self.group = group

    @property
    def parse(self):
        if DataElementFormat(self.elements).struct == "list(list(str,str,str,str,str))":
            if self.group is None:
                y = [
                    ["C506:1153M", "an3", self.elements[0][0]],
                    ["C506:1154M", "an25", self.elements[0][1]],
                    ["C506:1060C", "an3", self.elements[0][4]],
                ]

                return {
                    "segment": self.tag,
                    "segment_description": "Reference",
                    "segment_function": "Transaction Reference Number",
                    "group": self.group,
                    "group_description": None,
                    "group_usage": None,
                    "level": 0,
                    "usage": "C",
                    "max_use": 1,
                    "purpose": "A segment to to specify message reference.",
                    "elements": DataElementFormat(y).process,
                }

        elif DataElementFormat(self.elements).struct == "list(list(str,str))":
            if self.group == "Segment Group 4":
                y = [
                    ["C506:1153M", "an3", self.elements[0][0]],
                    ["C506:1154M", "an25", self.elements[0][1]],
                ]

                return {
                    "segment": self.tag,
                    "segment_description": "Reference",
                    "segment_function": "Traveler Identification",
                    "group": self.group,
                    "group_description": "Name and Address",
                    "group_usage": "C",
                    "level": 2,
                    "usage": "C",
                    "max_use": 9,
                    "purpose": "A segment specifying the number assigned by an Aircraft Operator that identifies a passenger's reservation.",
                    "elements": DataElementFormat(y).process,
                }
