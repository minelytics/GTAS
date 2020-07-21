from gtas.parsers.paxlst.data_element_format import DataElementFormat


class LOC:
    def __init__(self, collections, group):
        self.tag = collections.segments[0].tag
        self.elements = collections.segments[0].elements
        self.group = group

    @property
    def parse(self):
        if DataElementFormat(self.elements).struct == "list(str,str)":
            if self.group == "Segment Group 3":
                y = [
                    ["3227M", "n3", self.elements[0]],
                    ["C517:3225M", "an3", self.elements[1]],
                ]

                return {
                    "segment": self.tag,
                    "segment_description": "Place/Location Identification",
                    "segment_function": "Flight Itinerary",
                    "group": self.group,
                    "group_description": "Place/Location Identification",
                    "group_usage": "C",
                    "level": 2,
                    "usage": "M",
                    "max_use": 1,
                    "purpose": "A segment to specify locations such as place of departure, place of destination, country of ultimate destination, country and/or place of transit, country of transit termination, etc. of a passenger/crew.",
                    "elements": DataElementFormat(y).process,
                }

            elif self.group == "Segment Group 4":
                y = [
                    ["3227M", "an3", self.elements[0]],
                    ["C517:3225M", "an3", self.elements[1]],
                ]

                return {
                    "segment": self.tag,
                    "segment_description": "Place/Location Identification",
                    "segment_function": "Residence/Itinerary/Birth",
                    "group": self.group,
                    "group_description": "Name and Address",
                    "group_usage": "C",
                    "level": 2,
                    "usage": "C",
                    "max_use": 5,
                    "purpose": "A segment indicating country of birth and port/place of origin (embarkation), transit and destination (debarkation) of a passenger and/or crew.",
                    "elements": DataElementFormat(y).process,
                }

            elif self.group == "Segment Group 5":
                y = [
                    ["3227M", "an3", self.elements[0]],
                    ["C517:3225M", "an3", self.elements[1]],
                ]

                return {
                    "segment": self.tag,
                    "segment_description": "Place/Location Identification",
                    "segment_function": "Document Issuing Country",
                    "group": self.group,
                    "group_description": "Document/Message Details",
                    "group_usage": "C",
                    "level": 3,
                    "usage": "C",
                    "max_use": 1,
                    "purpose": "A segment indicating the country that issued the document.",
                    "elements": DataElementFormat(y).process,
                }

        elif (
            DataElementFormat(self.elements).struct
            == "list(str,str,list(str,str,str,str),list(str,str,str,str))"
        ):
            if self.group == "Segment Group 4":
                y = [
                    ["3227M", "an3", self.elements[0]],
                    ["C517:3225M", "an3", self.elements[1]],
                    ["C519:3222C", "an70", self.elements[2][3]],
                    ["C553:3232C", "an70", self.elements[3][3]],
                ]

                return {
                    "segment": self.tag,
                    "segment_description": "Place/Location Identification",
                    "segment_function": "Residence/Itinerary/Birth",
                    "group": self.group,
                    "group_description": "Name and Address",
                    "group_usage": "C",
                    "level": 2,
                    "usage": "C",
                    "max_use": 5,
                    "purpose": "A segment indicating country of birth and port/place of origin (embarkation), transit and destination (debarkation) of a passenger and/or crew.",
                    "elements": DataElementFormat(y).process,
                }
