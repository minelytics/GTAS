import pytest
from pydifact import Message

from gtas.parsers.paxlst.segment.com import COM


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()

    message = "COM+703 555 1234:TE+703 555 9876:FX'"
    setup.message = Message.from_str(message)
    setup.expected = {
        "segment": "COM",
        "segment_description": "Communication Contact",
        "segment_function": "Reporting Party Contact Information",
        "group": "Segment Group 1",
        "group_description": "Name and Address",
        "group_usage": "C",
        "level": 2,
        "usage": "C",
        "max_use": 1,
        "purpose": "A segment to identify communication numbers of departments or persons to whom communication should be directed (e.g., telephone, fax number).",
        "elements": [
            {
                "data_element_tag": "C076:3148",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 20,
                "data_value": "703 555 1234",
                "description": "Communication Address Identifier",
            },
            {
                "data_element_tag": "C076:3155",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "TE",
                "description": "Communication Address Code Qualifier",
            },
            {
                "data_element_tag": "C076:3148",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 20,
                "data_value": "703 555 9876",
                "description": "Communication Address Identifier",
            },
            {
                "data_element_tag": "C076:3155",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "FX",
                "description": "Communication Address Code Qualifier",
            },
        ],
    }

    return setup


class TestCOM:
    def test_com(self, setup):
        parsed = COM(setup.message, "Segment Group 1").parse
        assert parsed == setup.expected
