import pytest
from pydifact import Message

from gtas.parsers.paxlst.segment.une import UNE


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()

    message = "UNE+1+100'"
    setup.message = Message.from_str(message)
    setup.expected = {
        "segment": "UNE",
        "segment_description": "Functional Group Trailer",
        "segment_function": "Group Trailer",
        "group": None,
        "group_description": None,
        "group_usage": None,
        "level": 0,
        "usage": "C",
        "max_use": 1,
        "purpose": "To end and check the completeness of a Functional Group.",
        "elements": [
            {
                "data_element_tag": "0060",
                "segment_requirement": "M",
                "data_element_type": "n",
                "max_length": 6,
                "data_value": "1",
                "description": "Group Control Count",
            },
            {
                "data_element_tag": "0048",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 14,
                "data_value": "100",
                "description": "Group Reference Number",
            },
        ],
    }

    return setup


class TestUNE:
    def test_une(self, setup):
        parsed = UNE(setup.message).parse
        assert parsed == setup.expected
