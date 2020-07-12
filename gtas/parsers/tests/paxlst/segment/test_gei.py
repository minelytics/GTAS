import pytest
from pydifact import Message

from gtas.parsers.paxlst.segment.gei import GEI


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()

    message = "GEI+4+ZZZ'"
    setup.message = Message.from_str(message)
    setup.expected = {
        "segment": "GEI",
        "segment_description": "Processing Information",
        "segment_function": "Verification Indicator",
        "group": "Segment Group 4",
        "group_description": "Name and Address",
        "group_usage": "C",
        "level": 2,
        "usage": "C",
        "max_use": 2,
        "purpose": "A segment to specify indicators such as risk assessment.",
        "elements": [
            {
                "data_element_tag": "9649",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "4",
                "description": "Processing Information Code Qualifier",
            },
            {
                "data_element_tag": "C012:7365",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "ZZZ",
                "description": "Processing Indicator Description Code",
            },
        ],
    }

    return setup


class TestGEI:
    def test_gei(self, setup):
        parsed = GEI(setup.message, "Segment Group 4").parse
        assert parsed == setup.expected
