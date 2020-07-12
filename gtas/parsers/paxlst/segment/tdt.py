from gtas.parsers.paxlst.data_element_format import DataElementFormat
from gtas.parsers.paxlst.elements_structure import ElementsStructure


class TDT:
    def __init__(self, collections):
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements

    @property
    def parse(self):
        if ElementsStructure(self.elements).struct == "list(str,str,str,str,str)":
            y = [
                ["8051M", "an3", self.elements[0]],
                ["8028C", "an8", self.elements[1]],
                ["C040:3127C", "an17", self.elements[4]],
            ]

            return {
                "segment": self.tag,
                "segment_description": "Transport Information",
                "group": "Segment Group 2",
                "group_description": "Transport Information",
                "group_usage": "M",
                "level": 1,
                "usage": "M",
                "max_use": 10,
                "purpose": "A segment to specify details of transport related to each leg, including means of transport, mode of transport name and/or number of vessel and/or vehicle and/or flight.",
                "elements": DataElementFormat(y).process,
            }
