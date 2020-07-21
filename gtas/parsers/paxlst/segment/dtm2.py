from gtas.parsers.paxlst.element2 import Element


class DTM:
    def __init__(self, collections, group=None):
        self.elements = collections.segments[0].elements
        self.group = group

    @property
    def parse(self):
        output = {
            "segment": "DTM",
            "segment_description": "Date/Time/Period",
            "group": self.group,
        }
        output.update(self.segment_group(self.group))

        output["elements"].append(
            self.definition(
                data_element="C507",
                component_element="2005M",
                attributes="an..3",
                data=self.elements[0][0],
            )
        )
        output["elements"].append(
            self.definition(
                data_element="C507",
                component_element="2380M",
                attributes="n..10",
                data=self.elements[0][1],
            )
        )

        if Element().struct(self.elements) == "list(list(str,str,str))":
            output["elements"].append(
                self.definition(
                    data_element="C507",
                    component_element="2379C",
                    attributes="an..3",
                    data=self.elements[0][2],
                )
            )

        return output

    def segment_group(self, val):
        switch = {
            "Segment Group 3": {
                "segment_function": "Flight Leg Arrival/Departure",
                "group_description": "Place/Location Identification",
                "group_usage": "C",
                "level": 3,
                "usage": "C",
                "max_use": 1,
                "purpose": "A segment to specify associated dates and/or times as required related to locations.",
                "elements": [],
            },
            "Segment Group 4": {
                "segment_function": "Traveler Date of Birth",
                "group_description": "Name and Address",
                "group_usage": "C",
                "level": 2,
                "usage": "C",
                "max_use": 1,
                "purpose": "A segment to specify date of birth.",
                "elements": [],
            },
            "Segment Group 5": {
                "segment_function": "Flight Leg Arrival/Departure",
                "group_description": "Document/Message Details",
                "group_usage": "C",
                "level": 3,
                "usage": "C",
                "max_use": 1,
                "purpose": "A segment to specify associated dates/times related to documents.",
                "elements": [],
            },
        }
        return switch.get(val, "Incorrect Segment Group: {}".format(val))

    def definition(
        self, data_element=None, component_element=None, attributes=None, data=None
    ):
        if data_element is None:
            description = Element().description(component_element)
        else:
            description = Element().description(
                ":".join([data_element, component_element])
            )

        return {
            "data_element": data_element,
            "component_element": component_element,
            "attributes": attributes,
            "data": data,
            "description": description,
        }
