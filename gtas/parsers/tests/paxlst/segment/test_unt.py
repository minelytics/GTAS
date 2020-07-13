import pytest
from pydifact import Message

from gtas.parsers.paxlst.segment.unt import UNT


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()

    message = "UNT+35+PAX001'"
    setup.message = Message.from_str(message)
    setup.expected = {
        "segment": "UNT",
        "segment_description": "Message Trailer",
        "segment_function": "Message Trailer",
        "group": None,
        "group_description": None,
        "group_usage": None,
        "level": 0,
        "usage": "M",
        "max_use": 1,
        "purpose": "A service segment ending a message, giving the total number of segments in the message (including the UNH & UNT) and the control reference number of the message.",
        "elements": [
            {
                "data_element_tag": "0074",
                "segment_requirement": "M",
                "data_element_type": "n",
                "max_length": 6,
                "data_value": "35",
                "description": "Number of segments in a Message",
            },
            {
                "data_element_tag": "0062",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 14,
                "data_value": "PAX001",
                "description": "Message Reference Number",
            },
        ],
    }

    return setup


class TestUNT:
    def test_unt(self, setup):
        parsed = UNT(setup.message).parse
        assert parsed == setup.expected
