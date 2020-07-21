from gtas.parsers.paxlst.data_element_format import DataElementFormat
from gtas.parsers.paxlst.elements_structure import DataElementFormat


class UNZ:
    def __init__(self, collections, group=None):
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements
        self.group = group

    @property
    def parse(self):
        if DataElementFormat(self.elements).struct == "list(str,str)":
            if self.group is None:
                y = [
                    ["0036M", "n6", self.elements[0]],
                    ["0020M", "an14", self.elements[1]],
                ]

                return {
                    "segment": self.tag,
                    "segment_description": "Interchange Trailer",
                    "segment_function": "Interchange Trailer",
                    "group": self.group,
                    "group_description": None,
                    "group_usage": None,
                    "level": 0,
                    "usage": "M",
                    "max_use": 1,
                    "purpose": "To end and check the completeness of an interchange.",
                    "elements": DataElementFormat(y).process,
                }
