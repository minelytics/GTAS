import pytest
from pydifact import Message

from gtas.parsers.paxlst.segment.bgm import BGM


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()
    message = "BGM+745+CP'"
    setup.message = Message.from_str(message)

    setup.expected = {
        "segment": "BGM",
        "segment_description": "Beginning of Message",
        "segment_function": "Beginning of Message",
        "group": None,
        "group_description": None,
        "group_usage": None,
        "level": 0,
        "usage": "M",
        "max_use": 1,
        "purpose": "A segment to indicate the type and function of the message.",
        "elements": [
            {
                "data_element_tag": "C002:1001",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "745",
                "description": "Document Name Code",
            },
            {
                "data_element_tag": "C106:1004",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 35,
                "data_value": "CP",
                "description": "Document Identifier",
            },
        ],
    }

    return setup


class TestBGM:
    def test_bgm(self, setup):
        parsed = BGM(setup.message).parse
        assert parsed == setup.expected
