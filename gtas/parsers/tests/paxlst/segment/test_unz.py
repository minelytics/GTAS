import pytest
from pydifact import Message

from gtas.parsers.paxlst.segment.unz import UNZ


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()

    message = "UNZ+1+000000001'"
    setup.message = Message.from_str(message)
    setup.expected = {
        "segment": "UNZ",
        "segment_description": "Interchange Trailer",
        "segment_function": "Interchange Trailer",
        "group": None,
        "group_description": None,
        "group_usage": None,
        "level": 0,
        "usage": "M",
        "max_use": 1,
        "purpose": "To end and check the completeness of an interchange.",
        "elements": [
            {
                "data_element_tag": "0036",
                "segment_requirement": "M",
                "data_element_type": "n",
                "max_length": 6,
                "data_value": "1",
                "description": "Interchange Control Count",
            },
            {
                "data_element_tag": "0020",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 14,
                "data_value": "000000001",
                "description": "Interchange Control Reference",
            },
        ],
    }

    return setup


class TestUNZ:
    def test_unz(self, setup):
        parsed = UNZ(setup.message).parse
        assert parsed == setup.expected
