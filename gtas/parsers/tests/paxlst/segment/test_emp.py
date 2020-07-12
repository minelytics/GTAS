import pytest
from pydifact import Message

from gtas.parsers.paxlst.segment.emp import EMP


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()

    message = "EMP+1+CR1:110:111'"
    setup.message = Message.from_str(message)
    setup.expected = {
        "segment": "EMP",
        "segment_description": "Employment Details",
        "segment_function": "Crew Member Status/Function",
        "group": "Segment Group 4",
        "group_description": "Name and Address",
        "group_usage": "C",
        "level": 2,
        "usage": "C",
        "max_use": 1,
        "purpose": "A segment to indicate the occupation of a passenger or the rank of crew.",
        "elements": [
            {
                "data_element_tag": "9003",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 1,
                "data_value": "1",
                "description": "Employment Details Qualifier Code",
            },
            {
                "data_element_tag": "C948:9005",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "CR1",
                "description": "Employment Category Description Code",
            },
            {
                "data_element_tag": "C948:1131",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "110",
                "description": "Code List Identification Code",
            },
            {
                "data_element_tag": "C948:3055",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "111",
                "description": "Code List Responsible Agency Code",
            },
        ],
    }

    return setup


class TestEMP:
    def test_emp(self, setup):
        parsed = EMP(setup.message, "Segment Group 4").parse
        assert parsed == setup.expected
