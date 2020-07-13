import pytest
from pydifact import Message

from gtas.parsers.paxlst.segment.loc import LOC


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()

    message1 = "LOC+125+YVR'"
    setup.message1 = Message.from_str(message1)
    setup.expected1 = {
        "segment": "LOC",
        "segment_description": "Place/Location Identification",
        "segment_function": "Flight Itinerary",
        "group": "Segment Group 3",
        "group_description": "Place/Location Identification",
        "group_usage": "C",
        "level": 2,
        "usage": "M",
        "max_use": 1,
        "purpose": "A segment to specify locations such as place of departure, place of destination, country of ultimate destination, country and/or place of transit, country of transit termination, etc. of a passenger/crew.",
        "elements": [
            {
                "data_element_tag": "3227",
                "segment_requirement": "M",
                "data_element_type": "n",
                "max_length": 3,
                "data_value": "125",
                "description": "Location Function Code Qualifier",
            },
            {
                "data_element_tag": "C517:3225",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "YVR",
                "description": "Location Name Code",
            },
        ],
    }

    message2 = "LOC+180+USA+:::ANYCITY+:::ANYSTATE'"
    setup.message2 = Message.from_str(message2)
    setup.expected2 = {
        "segment": "LOC",
        "segment_description": "Place/Location Identification",
        "segment_function": "Residence/Itinerary/Birth",
        "group": "Segment Group 4",
        "group_description": "Name and Address",
        "group_usage": "C",
        "level": 2,
        "usage": "C",
        "max_use": 5,
        "purpose": "A segment indicating country of birth and port/place of origin (embarkation), transit and destination (debarkation) of a passenger and/or crew.",
        "elements": [
            {
                "data_element_tag": "3227",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "180",
                "description": "Location Function Code Qualifier",
            },
            {
                "data_element_tag": "C517:3225",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "USA",
                "description": "Location Name Code",
            },
            {
                "data_element_tag": "C519:3222",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 70,
                "data_value": "ANYCITY",
                "description": "First Related Location Name",
            },
            {
                "data_element_tag": "C553:3232",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 70,
                "data_value": "ANYSTATE",
                "description": "Second Related Location Name",
            },
        ],
    }

    message3 = "LOC+174+CAN'"
    setup.message3 = Message.from_str(message3)
    setup.expected3 = {
        "segment": "LOC",
        "segment_description": "Place/Location Identification",
        "segment_function": "Residence/Itinerary/Birth",
        "group": "Segment Group 4",
        "group_description": "Name and Address",
        "group_usage": "C",
        "level": 2,
        "usage": "C",
        "max_use": 5,
        "purpose": "A segment indicating country of birth and port/place of origin (embarkation), transit and destination (debarkation) of a passenger and/or crew.",
        "elements": [
            {
                "data_element_tag": "3227",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "174",
                "description": "Location Function Code Qualifier",
            },
            {
                "data_element_tag": "C517:3225",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "CAN",
                "description": "Location Name Code",
            },
        ],
    }

    message4 = "LOC+91+CAN'"
    setup.message4 = Message.from_str(message4)
    setup.expected4 = {
        "segment": "LOC",
        "segment_description": "Place/Location Identification",
        "segment_function": "Document Issuing Country",
        "group": "Segment Group 5",
        "group_description": "Document/Message Details",
        "group_usage": "C",
        "level": 3,
        "usage": "C",
        "max_use": 1,
        "purpose": "A segment indicating the country that issued the document.",
        "elements": [
            {
                "data_element_tag": "3227",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "91",
                "description": "Location Function Code Qualifier",
            },
            {
                "data_element_tag": "C517:3225",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "CAN",
                "description": "Location Name Code",
            },
        ],
    }

    return setup


class TestLOC:
    def test_loc1(self, setup):
        parsed = LOC(setup.message1, "Segment Group 3").parse
        assert parsed == setup.expected1

    def test_loc2(self, setup):
        parsed = LOC(setup.message2, "Segment Group 4").parse
        assert parsed == setup.expected2

    def test_loc3(self, setup):
        parsed = LOC(setup.message3, "Segment Group 4").parse
        assert parsed == setup.expected3

    def test_loc4(self, setup):
        parsed = LOC(setup.message4, "Segment Group 5").parse
        assert parsed == setup.expected4
