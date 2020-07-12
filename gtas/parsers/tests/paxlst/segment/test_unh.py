import pytest
from pydifact import Message

from gtas.parsers.paxlst.segment.unh import UNH


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()
    message = "UNH+PAX001+PAXLST:D:05B:UN:IATA+API01+01'"
    setup.message = Message.from_str(message)

    setup.expected = {
        "segment": "UNH",
        "segment_description": "Message Header",
        "group": None,
        "group_description": None,
        "level": 0,
        "usage": "Mandatory",
        "max_use": 1,
        "purpose": "A service segment starting and uniquely identifying a message. The message type code for the Passenger list message is PAXLST.",
        "elements": [
            {
                "data_element_tag": "0062",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 14,
                "data_value": "PAX001",
                "description": "Message Reference Number",
            },
            {
                "data_element_tag": "S009:0065",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 6,
                "data_value": "PAXLST",
                "description": "Message Type Identifier",
            },
            {
                "data_element_tag": "S009:0052",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 1,
                "data_value": "D",
                "description": "Message Type Version",
            },
            {
                "data_element_tag": "S009:0054",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "05B",
                "description": "Message Type Release Number",
            },
            {
                "data_element_tag": "S009:0051",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 2,
                "data_value": "UN",
                "description": "Controlling Agency",
            },
            {
                "data_element_tag": "S009:0057",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 4,
                "data_value": "IATA",
                "description": "Association Assigned Code",
            },
            {
                "data_element_tag": "0068",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 35,
                "data_value": "API01",
                "description": "Common Access Reference",
            },
            {
                "data_element_tag": "S010:0070",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 2,
                "data_value": "01",
                "description": "Sequence Message Transfer Number",
            },
            {
                "data_element_tag": "S010:0073",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 1,
                "data_value": None,
                "description": "First/Last Message Transfer Indicator",
            },
        ],
    }

    return setup


class TestUNH:
    def test_unh(self, setup):
        parsed = UNH(setup.message).parse
        assert parsed == setup.expected
