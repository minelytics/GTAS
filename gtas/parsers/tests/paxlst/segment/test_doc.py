import pytest
from pydifact import Message

from gtas.parsers.paxlst.segment.doc import DOC


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()

    message = "DOC+P:110:111+MB1402411'"
    setup.message = Message.from_str(message)
    setup.expected = {
        "segment": "DOC",
        "segment_description": "Document/Message Details",
        "segment_function": "Traveler Document(s)",
        "group": "Segment Group 5",
        "group_description": "Document/Message Details",
        "group_usage": "C",
        "level": 2,
        "usage": "M",
        "max_use": 1,
        "purpose": "A segment identifying passenger and/or crew travel documents, such as passports, visas etc.",
        "elements": [
            {
                "data_element_tag": "C002:1001",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "P",
                "description": "Document Name Code",
            },
            {
                "data_element_tag": "C002:1131",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "110",
                "description": "Code List Identification Code",
            },
            {
                "data_element_tag": "C002:3055",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "111",
                "description": "Code List Responsible Agency Code",
            },
            {
                "data_element_tag": "C503:1004",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 35,
                "data_value": "MB1402411",
                "description": "Document Identifier",
            },
        ],
    }

    return setup


class TestDOC:
    def test_doc(self, setup):
        parsed = DOC(setup.message, "Segment Group 5").parse
        assert parsed == setup.expected
