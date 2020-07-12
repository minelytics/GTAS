import pytest
from pydifact import Message

from gtas.parsers.paxlst.segment.nad import NAD


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()
    message = "NAD+MS+++JACKSON'"
    setup.message = Message.from_str(message)

    setup.expected = {
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

    return setup


class TestNAD:
    def test_nad(self, setup):
        parsed = NAD(setup.message).parse
        assert parsed == setup.expected
