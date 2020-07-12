import pytest
from pydifact import Message

from gtas.parsers.paxlst.segment.unb import UNB


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()
    message = "UNB+UNOA:4+APIS*ABE+USADHS+070429:0900+000000001++USADHS'"
    setup.message = Message.from_str(message)

    setup.expected = {
        "segment_group": "header",
        "segment_tag": "UNB",
        "segment_elements": [
            {
                "data_element_tag": "S001:0001",
                "segment_requirement": "M",
                "data_element_type": "a",
                "max_length": 4,
                "data_value": "UNOA",
                "description": "Syntax Identifier",
            },
            {
                "data_element_tag": "S001:0002",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 1,
                "data_value": "4",
                "description": "Syntax Version Number",
            },
            {
                "data_element_tag": "S002:0004",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 35,
                "data_value": "APIS*ABE",
                "description": "Interchange Sender Identification",
            },
            {
                "data_element_tag": "S002:0007",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 2,
                "data_value": "ZZ",
                "description": "Identification Code Qualifier",
            },
            {
                "data_element_tag": "S003:0010",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 35,
                "data_value": "USADHS",
                "description": "Interchange Recipient Identification",
            },
            {
                "data_element_tag": "S003:0007",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 2,
                "data_value": "ZZ",
                "description": "Identification Code Qualifier",
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
                "data_element_tag": "0020",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 14,
                "data_value": "000000001",
                "description": "Interchange Control Reference",
            },
            {
                "data_element_tag": "0026",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 14,
                "data_value": "USADHS",
                "description": "Application Reference",
            },
        ],
    }

    return setup


class TestUNB:
    def test_unb(self, setup):
        parsed = UNB("header", setup.message).parse
        assert parsed == setup.expected
