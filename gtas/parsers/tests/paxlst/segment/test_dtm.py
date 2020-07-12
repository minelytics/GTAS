import pytest
from pydifact import Message

from gtas.parsers.paxlst.segment.dtm import DTM


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()
    message = "DTM+189:0704291230:201'"
    setup.message = Message.from_str(message)

    setup.expected = {
        "segment": "DTM",
        "segment_description": "Date/Time/Period",
        "group": "Segment Group 3",
        "group_description": "Place/Location Identification",
        "group_usage": "C",
        "level": 3,
        "usage": "C",
        "max_use": 1,
        "purpose": "A segment to specify associated dates and/or times as required related to locations.",
        "elements": [
            {
                "data_element_tag": "C507:2005",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "189",
                "description": "Date/Time/Period Function Code Qualifier",
            },
            {
                "data_element_tag": "C507:2380",
                "segment_requirement": "M",
                "data_element_type": "n",
                "max_length": 10,
                "data_value": "0704291230",
                "description": "Date/Time/Period Value",
            },
            {
                "data_element_tag": "C507:2379",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "201",
                "description": "Date/Time/Period Format Code",
            },
        ],
    }

    return setup


class TestDTM:
    def test_dtm(self, setup):
        parsed = DTM(setup.message).parse
        assert parsed == setup.expected
