import pytest
from pydifact import Message

from gtas.parsers.paxlst.segment.ung import UNG


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()
    message = "UNG+PAXLST+XYZ AIRLINES+USADHS+070429:0900+100+UN+D:05B'"
    setup.message = Message.from_str(message)

    setup.expected = {
        "segment": "UNG",
        "segment_description": "Functional Group Header",
        "group": None,
        "group_description": None,
        "group_usage": None,
        "level": 0,
        "usage": "C",
        "max_use": 1,
        "purpose": "To begin a group of like transaction. Only one grouping of transactions will be allowed for this implementation.",
        "elements": [
            {
                "data_element_tag": "0038",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 6,
                "data_value": "PAXLST",
                "description": "Message Group Identification",
            },
            {
                "data_element_tag": "S006:0040",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 35,
                "data_value": "XYZ AIRLINES",
                "description": "Application Sender Identifier",
            },
            {
                "data_element_tag": "S007:0044",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 35,
                "data_value": "USADHS",
                "description": "Application Recipient Identification",
            },
            {
                "data_element_tag": "S004:0017",
                "segment_requirement": "M",
                "data_element_type": "n",
                "max_length": 6,
                "data_value": "070429",
                "description": "Date",
            },
            {
                "data_element_tag": "S004:0019",
                "segment_requirement": "M",
                "data_element_type": "n",
                "max_length": 4,
                "data_value": "0900",
                "description": "Time",
            },
            {
                "data_element_tag": "0048",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 14,
                "data_value": "100",
                "description": "Group Reference Number",
            },
            {
                "data_element_tag": "0051",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 2,
                "data_value": "UN",
                "description": "Controlling Agency",
            },
            {
                "data_element_tag": "S008:0052",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 1,
                "data_value": "D",
                "description": "Message Version Number",
            },
            {
                "data_element_tag": "S008:0054",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "05B",
                "description": "Message Release Number",
            },
        ],
    }

    return setup


class TestUNG:
    def test_ung(self, setup):
        parsed = UNG(setup.message).parse
        assert parsed == setup.expected
