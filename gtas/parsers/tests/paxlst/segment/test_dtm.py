import pytest
from pydifact import Message

from gtas.parsers.paxlst.segment.dtm import DTM


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
        "segment_function": "Flight Leg Arrival/Departure",
        "group": "Segment Group 3",
        "group_description": "Place/Location Identification",
        "group_usage": "C",
        "level": 3,
        "usage": "C",
        "max_use": 1,
        "purpose": "A segment to specify associated dates and/or times as required related to locations.",
        "elements": [
            {
                "data_element_tag": "C507:2005",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "189",
                "description": "Date/Time/Period Function Code Qualifier",
            },
            {
                "data_element_tag": "C507:2380",
                "segment_requirement": "M",
                "data_element_type": "n",
                "max_length": 10,
                "data_value": "0704291230",
                "description": "Date/Time/Period Value",
            },
            {
                "data_element_tag": "C507:2379",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "201",
                "description": "Date/Time/Period Format Code",
            },
        ],
    }

    message2 = "DTM+329:570121'"
    setup.message2 = Message.from_str(message2)
    setup.expected2 = {
        "segment": "DTM",
        "segment_description": "Date/Time/Period",
        "segment_function": "Traveler Date of Birth",
        "group": "Segment Group 4",
        "group_description": "Name and Address",
        "group_usage": "C",
        "level": 2,
        "usage": "C",
        "max_use": 1,
        "purpose": "A segment to specify date of birth.",
        "elements": [
            {
                "data_element_tag": "C507:2005",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "329",
                "description": "Date/Time/Period Function Code Qualifier",
            },
            {
                "data_element_tag": "C507:2380",
                "segment_requirement": "M",
                "data_element_type": "n",
                "max_length": 6,
                "data_value": "570121",
                "description": "Date/Time/Period Value",
            },
        ],
    }

    return setup


class TestDTM:
    def test_dtm1(self, setup):
        parsed = DTM(setup.message1).parse
        assert parsed == setup.expected1

    def test_dtm2(self, setup):
        parsed = DTM(setup.message2).parse
        assert parsed == setup.expected2
