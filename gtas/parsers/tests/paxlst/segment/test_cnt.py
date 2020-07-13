import pytest
from pydifact import Message

from gtas.parsers.paxlst.segment.cnt import CNT


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()

    message = "CNT+42:9'"
    setup.message = Message.from_str(message)
    setup.expected = {
        "segment": "CNT",
        "segment_description": "Control Total",
        "segment_function": "Control Total",
        "group": None,
        "group_description": None,
        "group_usage": None,
        "level": 0,
        "usage": "C",
        "max_use": 1,
        "purpose": "A segment specifying control totals such as the total number of passengers/ crew members in the message.",
        "elements": [
            {
                "data_element_tag": "C270:6069",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "42",
                "description": "Control Total Type Code Qualifier",
            },
            {
                "data_element_tag": "C270:6066",
                "segment_requirement": "M",
                "data_element_type": "n",
                "max_length": 18,
                "data_value": "9",
                "description": "Control Total Value",
            },
        ],
    }

    return setup


class TestCNT:
    def test_cnt(self, setup):
        parsed = CNT(setup.message).parse
        assert parsed == setup.expected
