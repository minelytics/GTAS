import pytest
from pydifact import Message

from gtas.parsers.paxlst.segment.nad import NAD


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()

    message1 = "NAD+MS+++JACKSON'"
    setup.message1 = Message.from_str(message1)
    setup.expected1 = {
        "segment": "NAD",
        "segment_description": "Name and Address",
        "segment_function": "Reporting Party",
        "group": "Segment Group 1",
        "group_description": "Name and Address",
        "group_usage": "C",
        "level": 1,
        "usage": "M",
        "max_use": 1,
        "purpose": "A segment to identify the name, address and related function.",
        "elements": [
            {
                "data_element_tag": "3035",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 2,
                "data_value": "MS",
                "description": "Party Function Code Qualifier",
            },
            {
                "data_element_tag": "C080:3036",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 35,
                "data_value": "JACKSON",
                "description": "Party Name",
            },
        ],
    }

    message2 = "NAD+FL+++DOE:JOHN WAYNE+20 MAIN ST+ANYCITY+VA+10053+USA'"
    setup.message2 = Message.from_str(message2)
    setup.expected2 = {
        "segment": "NAD",
        "segment_description": "Name and Address",
        "segment_function": "Traveler Identification",
        "group": "Segment Group 4",
        "group_description": "Name and Address",
        "group_usage": "C",
        "level": 1,
        "usage": "M",
        "max_use": 1,
        "purpose": "A segment specifying name of the passenger or crew member.",
        "elements": [
            {
                "data_element_tag": "3035",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "FL",
                "description": "Party Function Code Qualifier",
            },
            {
                "data_element_tag": "C080:3036",
                "segment_requirement": "C",
                "data_element_type": "a",
                "max_length": 35,
                "data_value": "DOE",
                "description": "Party Name",
            },
            {
                "data_element_tag": "C080:3036",
                "segment_requirement": "C",
                "data_element_type": "a",
                "max_length": 35,
                "data_value": "JOHN WAYNE",
                "description": "Party Name",
            },
            {
                "data_element_tag": "C059:3042",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 35,
                "data_value": "20 MAIN ST",
                "description": "Number and Street Identifier",
            },
            {
                "data_element_tag": "3164",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 35,
                "data_value": "ANYCITY",
                "description": "City Name",
            },
            {
                "data_element_tag": "C819:3229",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 2,
                "data_value": "VA",
                "description": "Country Sub-entity Name Code",
            },
            {
                "data_element_tag": "3251",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 17,
                "data_value": "10053",
                "description": "Postal Identification Code",
            },
            {
                "data_element_tag": "3207",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "USA",
                "description": "Country Name Code",
            },
        ],
    }

    message3 = "NAD+FL+++DOE:JOHN:WAYNE+20 MAIN ST+ANYCITY+VA+10053+USA'"
    setup.message3 = Message.from_str(message3)
    setup.expected3 = {
        "segment": "NAD",
        "segment_description": "Name and Address",
        "segment_function": "Traveler Identification",
        "group": "Segment Group 4",
        "group_description": "Name and Address",
        "group_usage": "C",
        "level": 1,
        "usage": "M",
        "max_use": 1,
        "purpose": "A segment specifying name of the passenger or crew member.",
        "elements": [
            {
                "data_element_tag": "3035",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "FL",
                "description": "Party Function Code Qualifier",
            },
            {
                "data_element_tag": "C080:3036",
                "segment_requirement": "C",
                "data_element_type": "a",
                "max_length": 35,
                "data_value": "DOE",
                "description": "Party Name",
            },
            {
                "data_element_tag": "C080:3036",
                "segment_requirement": "C",
                "data_element_type": "a",
                "max_length": 35,
                "data_value": "JOHN",
                "description": "Party Name",
            },
            {
                "data_element_tag": "C080:3036",
                "segment_requirement": "C",
                "data_element_type": "a",
                "max_length": 35,
                "data_value": "WAYNE",
                "description": "Party Name",
            },
            {
                "data_element_tag": "C059:3042",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 35,
                "data_value": "20 MAIN ST",
                "description": "Number and Street Identifier",
            },
            {
                "data_element_tag": "3164",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 35,
                "data_value": "ANYCITY",
                "description": "City Name",
            },
            {
                "data_element_tag": "C819:3229",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 2,
                "data_value": "VA",
                "description": "Country Sub-entity Name Code",
            },
            {
                "data_element_tag": "3251",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 17,
                "data_value": "10053",
                "description": "Postal Identification Code",
            },
            {
                "data_element_tag": "3207",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "USA",
                "description": "Country Name Code",
            },
        ],
    }

    return setup


class TestNAD:
    def test_nad1(self, setup):
        parsed = NAD(setup.message1, "Segment Group 1").parse
        assert parsed == setup.expected1

    def test_nad2(self, setup):
        parsed = NAD(setup.message2, "Segment Group 4").parse
        assert parsed == setup.expected2

    def test_nad3(self, setup):
        parsed = NAD(setup.message3, "Segment Group 4").parse
        assert parsed == setup.expected3
