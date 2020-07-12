import pytest
from pydifact import Message

from gtas.parsers.paxlst.segment.nat import NAT


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()

    message = "NAT+2+CAN'"
    setup.message = Message.from_str(message)
    setup.expected = {
        "segment": "NAT",
        "segment_description": "Nationality",
        "segment_function": "Traveler Citizenship",
        "group": "Segment Group 4",
        "group_description": "Name and Address",
        "group_usage": "C",
        "level": 2,
        "usage": "C",
        "max_use": 1,
        "purpose": "A segment to indicate the nationality of a passenger and/or crew.",
        "elements": [
            {
                "data_element_tag": "3493",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 1,
                "data_value": "2",
                "description": "Nationality Code Qualifier",
            },
            {
                "data_element_tag": "C042:3293",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "CAN",
                "description": "Nationality Name Code",
            },
        ],
    }

    return setup


class TestNAT:
    def test_nat(self, setup):
        parsed = NAT(setup.message, "Segment Group 4").parse
        assert parsed == setup.expected
