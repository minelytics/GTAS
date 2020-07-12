import pytest
from pydifact import Message

from gtas.parsers.paxlst.segment.att import ATT


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()

    message = "ATT+2++M'"
    setup.message = Message.from_str(message)
    setup.expected = {
        "segment": "ATT",
        "segment_description": "Attribute",
        "segment_function": "Traveler Gender",
        "group": "Segment Group 4",
        "group_description": "Name and Address",
        "group_usage": "C",
        "level": 2,
        "usage": "C",
        "max_use": 1,
        "purpose": "A segment specifying passenger's and/or crew attributes such as complexion and build.",
        "elements": [
            {
                "data_element_tag": "9017",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 1,
                "data_value": "2",
                "description": "Attribute Function Code Qualifier",
            },
            {
                "data_element_tag": "C956:9019",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 1,
                "data_value": "M",
                "description": "Attribute Description Code",
            },
        ],
    }

    return setup


class TestATT:
    def test_att(self, setup):
        parsed = ATT(setup.message, "Segment Group 4").parse
        assert parsed == setup.expected
