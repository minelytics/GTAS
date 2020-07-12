import pytest
from pydifact import Message

from gtas.parsers.paxlst.segment.loc import LOC


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()
    message = "LOC+125+YVR'"
    setup.message = Message.from_str(message)

    setup.expected = {
        "segment": "LOC",
        "segment_description": "Place/Location Identification",
        "group": "Segment Group 3",
        "group_description": "Place/Location Identification",
        "group_usage": "C",
        "level": 2,
        "usage": "M",
        "max_use": 1,
        "purpose": "A segment to specify locations such as place of departure, place of destination, country of ultimate destination, country and/or place of transit, country of transit termination, etc. of a passenger/crew.",
        "elements": [
            {
                "data_element_tag": "3227",
                "segment_requirement": "M",
                "data_element_type": "n",
                "max_length": 3,
                "data_value": "125",
                "description": "Location Function Code Qualifier",
            },
            {
                "data_element_tag": "C517:3225",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "YVR",
                "description": "Location Name Code",
            },
        ],
    }

    return setup


class TestLOC:
    def test_loc(self, setup):
        parsed = LOC(setup.message).parse
        assert parsed == setup.expected
