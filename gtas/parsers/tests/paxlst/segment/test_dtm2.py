import pytest
from pydifact import Message

from gtas.parsers.paxlst.segment.dtm2 import DTM


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()

    message1 = "DTM+189:0704291230:201'"
    setup.message1 = Message.from_str(message1)
    setup.expected1 = {
        "segment": "DTM",
        "segment_description": "Date/Time/Period",
        "group": "Segment Group 3",
        "segment_function": "Flight Leg Arrival/Departure",
        "group_description": "Place/Location Identification",
        "group_usage": "C",
        "level": 3,
        "usage": "C",
        "max_use": 1,
        "purpose": "A segment to specify associated dates and/or times as required related to locations.",
        "elements": [
            {
                "data_element": "C507",
                "component_element": "2005M",
                "attributes": "an..3",
                "data": "189",
                "description": "Date/Time/Period Function Code Qualifier",
            },
            {
                "data_element": "C507",
                "component_element": "2380M",
                "attributes": "n..10",
                "data": "0704291230",
                "description": "Date/Time/Period Value",
            },
            {
                "data_element": "C507",
                "component_element": "2379C",
                "attributes": "an..3",
                "data": "201",
                "description": "Date/Time/Period Format Code",
            },
        ],
    }

    message2 = "DTM+329:570121'"
    setup.message2 = Message.from_str(message2)
    setup.expected2 = {
        "segment": "DTM",
        "segment_description": "Date/Time/Period",
        "group": "Segment Group 4",
        "segment_function": "Traveler Date of Birth",
        "group_description": "Name and Address",
        "group_usage": "C",
        "level": 2,
        "usage": "C",
        "max_use": 1,
        "purpose": "A segment to specify date of birth.",
        "elements": [
            {
                "data_element": "C507",
                "component_element": "2005M",
                "attributes": "an..3",
                "data": "329",
                "description": "Date/Time/Period Function Code Qualifier",
            },
            {
                "data_element": "C507",
                "component_element": "2380M",
                "attributes": "n..10",
                "data": "570121",
                "description": "Date/Time/Period Value",
            },
        ],
    }

    message3 = "DTM+36:081021'"
    setup.message3 = Message.from_str(message3)
    setup.expected3 = {
        "segment": "DTM",
        "segment_description": "Date/Time/Period",
        "group": "Segment Group 5",
        "segment_function": "Traveler Document Expiration",
        "group_description": "Document/Message Details",
        "group_usage": "C",
        "level": 3,
        "usage": "C",
        "max_use": 1,
        "purpose": "A segment to specify associated dates/times related to documents.",
        "elements": [
            {
                "data_element": "C507",
                "component_element": "2005M",
                "attributes": "an..3",
                "data": "36",
                "description": "Date/Time/Period Function Code Qualifier",
            },
            {
                "data_element": "C507",
                "component_element": "2380M",
                "attributes": "n..10",
                "data": "081021",
                "description": "Date/Time/Period Value",
            },
        ],
    }

    return setup


class TestDTM:
    def test_dtm1(self, setup):
        parsed = DTM.parse(setup.message1, "Segment Group 3")
        assert parsed == setup.expected1

    def test_dtm2(self, setup):
        parsed = DTM.parse(setup.message2, "Segment Group 4")
        assert parsed == setup.expected2

    def test_dtm3(self, setup):
        parsed = DTM.parse(setup.message3, "Segment Group 5")
        assert parsed == setup.expected3
