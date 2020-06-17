from django.test import TestCase
from pydifact import Message

from gtas.parsers.paxlst import paxlst_parser


class LOCTest(TestCase):
    """Test for LOC Tag"""
    def setUp(self):
        """Pydifact parsed message"""
        self.collection1 = Message.from_str("LOC+125+IAD'")
        self.loc1 = {
            'tag': "LOC",
            'element': {
                "125": {
                    "DEPARTURE_AIRPORT": "IAD"
                }
            }
        }

        self.collection2 = Message.from_str("LOC+87+BRU'")
        self.loc2 = {
            'tag': "LOC",
            'element': {
                "87": {
                    "ARRIVAL_AIRPORT": "BRU"
                }
            }
        }

    def test_parser_loc1(self):
        """Test the parser output"""
        for segment in self.collection1.segments:
            cls = getattr(paxlst_parser, segment.tag)
            self.assertEqual("LOC", cls().tag(segment))
            self.assertEqual(self.loc1, cls().process(segment))

    def test_parser_loc2(self):
        """Test the parser output"""
        for segment in self.collection2.segments:
            cls = getattr(paxlst_parser, segment.tag)
            self.assertEqual("LOC", cls().tag(segment))
            self.assertEqual(self.loc2, cls().process(segment))

    def tearDown(self):
        del self.collection1
        del self.loc1
        del self.collection2
        del self.loc2


class DTMTest(TestCase):
    """Test for DTM Tag"""
    def setUp(self):
        self.collection1 = Message.from_str("DTM+189:2005061200:201'")
        self.dtm1 = {
            'tag': "DTM",
            'element': {
                "189": {
                    "DEPARTURE_DATETIME": "2020-05-06 12:00"
                }
            }
        }

    def test_parser_dtm1(self):
        """Test parser output"""
        for segment in self.collection1.segments:
            cls = getattr(paxlst_parser, segment.tag)
            self.assertEqual("DTM", cls().tag(segment))
            self.assertEqual(self.dtm1, cls().process(segment))
