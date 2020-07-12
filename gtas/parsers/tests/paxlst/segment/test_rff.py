import pytest
from pydifact import Message

from gtas.parsers.paxlst.segment.rff import RFF


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()

    message1 = "RFF+TN:BA123456789:::1'"
    setup.message1 = Message.from_str(message1)
    setup.expected1 = {
        "segment": "RFF",
        "segment_description": "Reference",
        "segment_function": "Transaction Reference Number",
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

    message2 = "RFF+AVF:ABC123'"
    setup.message2 = Message.from_str(message2)
    setup.expected2 = {
        "segment": "RFF",
        "segment_description": "Reference",
        "segment_function": "Traveler Identification",
        "group": "Segment Group 4",
        "group_description": "Name and Address",
        "group_usage": "C",
        "level": 2,
        "usage": "C",
        "max_use": 9,
        "purpose": "A segment specifying the number assigned by an Aircraft Operator that identifies a passenger's reservation.",
        "elements": [
            {
                "data_element_tag": "C506:1153",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "AVF",
                "description": "Reference Code Qualifier",
            },
            {
                "data_element_tag": "C506:1154",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 25,
                "data_value": "ABC123",
                "description": "Reference Identifier",
            },
        ],
    }

    return setup


class TestRFF:
    def test_rff1(self, setup):
        parsed = RFF(setup.message1).parse
        assert parsed == setup.expected1

    def test_rff2(self, setup):
        parsed = RFF(setup.message2, "Segment Group 4").parse
        assert parsed == setup.expected2
