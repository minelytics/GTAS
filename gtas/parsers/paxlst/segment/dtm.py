from gtas.parsers.paxlst.data_element_format import DataElementFormat


class DTM:
    def __init__(self, collections, group=None):
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements
        self.group = group

    @property
    def parse(self):
        if DataElementFormat(self.elements).struct == "list(list(str,str,str))":
            if self.group == "Segment Group 3":
                y = [
                    ["C507:2005M", "an3", self.elements[0][0]],
                    ["C507:2380M", "n10", self.elements[0][1]],
                    ["C507:2379C", "an3", self.elements[0][2]],
                ]

                return {
                    "segment": self.tag,
                    "segment_description": "Date/Time/Period",
                    "segment_function": "Flight Leg Arrival/Departure",
                    "group": self.group,
                    "group_description": "Place/Location Identification",
                    "group_usage": "C",
                    "level": 3,
                    "usage": "C",
                    "max_use": 1,
                    "purpose": "A segment to specify associated dates and/or times as required related to locations.",
                    "elements": DataElementFormat(y).process,
                }

        elif DataElementFormat(self.elements).struct == "list(list(str,str))":
            if self.group == "Segment Group 4":
                y = [
                    ["C507:2005M", "an3", self.elements[0][0]],
                    ["C507:2380M", "n6", self.elements[0][1]],
                ]

                return {
                    "segment": self.tag,
                    "segment_description": "Date/Time/Period",
                    "segment_function": "Traveler Date of Birth",
                    "group": self.group,
                    "group_description": "Name and Address",
                    "group_usage": "C",
                    "level": 2,
                    "usage": "C",
                    "max_use": 1,
                    "purpose": "A segment to specify date of birth.",
                    "elements": DataElementFormat(y).process,
                }

            elif self.group == "Segment Group 5":
                y = [
                    ["C507:2005M", "an3", self.elements[0][0]],
                    ["C507:2380M", "n6", self.elements[0][1]],
                ]

                return {
                    "segment": self.tag,
                    "segment_description": "Date/Time/Period",
                    "segment_function": "Traveler Document Expiration",
                    "group": self.group,
                    "group_description": "Document/Message Details",
                    "group_usage": "C",
                    "level": 3,
                    "usage": "C",
                    "max_use": 1,
                    "purpose": "A segment to specify associated dates/times related to documents.",
                    "elements": DataElementFormat(y).process,
                }
