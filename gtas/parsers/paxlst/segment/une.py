from gtas.parsers.paxlst.data_element_format import DataElementFormat


class UNE:
    def __init__(self, collections, group=None):
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements
        self.group = group

    @property
    def parse(self):
        if DataElementFormat(self.elements).struct == "list(str,str)":
            if self.group is None:
                y = [
                    ["0060M", "n6", self.elements[0]],
                    ["0048M", "an14", self.elements[1]],
                ]

                return {
                    "segment": self.tag,
                    "segment_description": "Functional Group Trailer",
                    "segment_function": "Group Trailer",
                    "group": self.group,
                    "group_description": None,
                    "group_usage": None,
                    "level": 0,
                    "usage": "C",
                    "max_use": 1,
                    "purpose": "To end and check the completeness of a Functional Group.",
                    "elements": DataElementFormat(y).process,
                }
