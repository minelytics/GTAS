from gtas.parsers.paxlst.data_element_format import DataElementFormat


class UNT:
    def __init__(self, collections, group=None):
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements
        self.group = group

    @property
    def parse(self):
        if DataElementFormat(self.elements).struct == "list(str,str)":
            if self.group is None:
                y = [
                    ["0074M", "n6", self.elements[0]],
                    ["0062M", "an14", self.elements[1]],
                ]

                return {
                    "segment": self.tag,
                    "segment_description": "Message Trailer",
                    "segment_function": "Message Trailer",
                    "group": self.group,
                    "group_description": None,
                    "group_usage": None,
                    "level": 0,
                    "usage": "M",
                    "max_use": 1,
                    "purpose": "A service segment ending a message, giving the total number of segments in the message (including the UNH & UNT) and the control reference number of the message.",
                    "elements": DataElementFormat(y).process,
                }
