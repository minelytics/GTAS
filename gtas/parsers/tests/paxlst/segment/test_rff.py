import pytest
from pydifact import Message

from gtas.parsers.paxlst.segment.rff import RFF


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()
    message = "RFF+TN:BA123456789:::1'"
    setup.message = Message.from_str(message)

    setup.expected = {
        "segment": "RFF",
        "segment_description": "Reference",
        "group": None,
        "group_description": None,
        "group_usage": None,
        "level": 0,
        "usage": "C",
        "max_use": 1,
        "purpose": "A segment to to specify message reference.",
        "elements": [
            {
                "data_element_tag": "C506:1153",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "TN",
                "description": "Reference Code Qualifier",
            },
            {
                "data_element_tag": "C506:1154",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 25,
                "data_value": "BA123456789",
                "description": "Reference Identifier",
            },
            {
                "data_element_tag": "C506:1060",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "1",
                "description": "Revision Identifier",
            },
        ],
    }

    return setup


class TestRFF:
    def test_rff(self, setup):
        parsed = RFF(setup.message).parse
        assert parsed == setup.expected
