import pytest
from pydifact import Message

from gtas.parsers.paxlst.segment.tdt import TDT


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()
    message = "TDT+20+UA123+++UA'"
    setup.message = Message.from_str(message)

    setup.expected = {
        "segment": "TDT",
        "segment_description": "Transport Information",
        "segment_function": "Flight Identification",
        "group": "Segment Group 2",
        "group_description": "Transport Information",
        "group_usage": "M",
        "level": 1,
        "usage": "M",
        "max_use": 10,
        "purpose": "A segment to specify details of transport related to each leg, including means of transport, mode of transport name and/or number of vessel and/or vehicle and/or flight.",
        "elements": [
            {
                "data_element_tag": "8051",
                "segment_requirement": "M",
                "data_element_type": "an",
                "max_length": 3,
                "data_value": "20",
                "description": "Transport Stage Qualifier",
            },
            {
                "data_element_tag": "8028",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 8,
                "data_value": "UA123",
                "description": "Means of Transport Journey Identifier",
            },
            {
                "data_element_tag": "C040:3127",
                "segment_requirement": "C",
                "data_element_type": "an",
                "max_length": 17,
                "data_value": "UA",
                "description": "Carrier Identifier",
            },
        ],
    }

    return setup


class TestTDT:
    def test_tdt(self, setup):
        parsed = TDT(setup.message).parse
        assert parsed == setup.expected
