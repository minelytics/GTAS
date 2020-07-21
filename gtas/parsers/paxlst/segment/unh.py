from gtas.parsers.paxlst.element import Element


class UNH:
    def __init__(self, collections, group=None):
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements
        self.group = group

    @property
    def parse(self):
        if (
            Element(self.elements).struct
            == "list(str,list(str,str,str,str,str),str,str)"
        ):
            if self.group is None:
                y = [
                    ["0062M", "an14", self.elements[0]],
                    ["S009:0065M", "an6", self.elements[1][0]],
                    ["S009:0052M", "an1", self.elements[1][1]],
                    ["S009:0054M", "an3", self.elements[1][2]],
                    ["S009:0051M", "an2", self.elements[1][3]],
                    ["S009:0057C", "an4", self.elements[1][4]],
                    ["0068C", "an35", self.elements[2]],
                    ["S010:0070C", "an2", self.elements[3]],
                    ["S010:0073C", "an1", None],
                ]

                return {
                    "segment": self.tag,
                    "segment_description": "Message Header",
                    "segment_function": "Message Header",
                    "group": self.group,
                    "group_description": None,
                    "group_usage": None,
                    "level": 0,
                    "usage": "M",
                    "max_use": 1,
                    "purpose": "A service segment starting and uniquely identifying a message. The message type code for the Passenger list message is PAXLST.",
                    "elements": Element(y).process,
                }
