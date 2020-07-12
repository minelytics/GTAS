import pytest
from pydifact import Message

from gtas.parsers.paxlst.segment.ftx import FTX


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()

    message1 = "FTX+BAG+++UA987654:3'"
    setup.message1 = Message.from_str(message1)
    setup.expected1 = {
        "segment": "FTX",
        "segment_description": "Free Text",
        "segment_function": "Bag Tag Identification Reporting",
        "group": "Segment Group 4",
        "group_description": "Error Point Details",
        "group_usage": "C",
        "level": 2,
        "usage": "C",
        "max_use": 99,
        "purpose": "A segment to provide explanation and/or supplementary information related to the specified application error.",
        "elements": [
            {
                "data_element_tag": "4451",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "BAG",
                "description": "Text Subject Code Qualifier",
            },
            {
                "data_element_tag": "C108:4440",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 80,
                "data_value": "UA987654",
                "description": "Text Literal",
            },
            {
                "data_element_tag": "C108:4440",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 80,
                "data_value": "3",
                "description": "Text Literal",
            },
        ],
    }

    message2 = "FTX+BAG+++UA123456'"
    setup.message2 = Message.from_str(message2)
    setup.expected2 = {
        "segment": "FTX",
        "segment_description": "Free Text",
        "segment_function": "Bag Tag Identification Reporting",
        "group": "Segment Group 4",
        "group_description": "Error Point Details",
        "group_usage": "C",
        "level": 2,
        "usage": "C",
        "max_use": 99,
        "purpose": "A segment to provide explanation and/or supplementary information related to the specified application error.",
        "elements": [
            {
                "data_element_tag": "4451",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "BAG",
                "description": "Text Subject Code Qualifier",
            },
            {
                "data_element_tag": "C108:4440",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 80,
                "data_value": "UA123456",
                "description": "Text Literal",
            },
        ],
    }

    return setup


class TestFTX:
    def test_ftx1(self, setup):
        parsed = FTX(setup.message1, "Segment Group 4").parse
        assert parsed == setup.expected1

    def test_ftx2(self, setup):
        parsed = FTX(setup.message2, "Segment Group 4").parse
        assert parsed == setup.expected2
