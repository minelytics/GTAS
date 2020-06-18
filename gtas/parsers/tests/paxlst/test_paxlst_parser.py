from django.test import TestCase
from pydifact import Message

from gtas.parsers.paxlst import paxlst_parser


class ATTTest(TestCase):
    """Test for ATT Tag"""
    def setUp(self):
        """Pydifact parsed message"""
        self.collection1 = Message.from_str("ATT+2++M'")
        self.att1 = {
            'tag': "ATT",
            'element': {
                "2": {
                    "GENDER": "M"
                }
            }
        }

        self.collection2 = Message.from_str("ATT+2++F'")
        self.att2 = {
            'tag': "ATT",
            'element': {
                "2": {
                    "GENDER": "F"
                }
            }
        }

    def test_parser_att1(self):
        """Test parser output"""
        for segment in self.collection1.segments:
            cls = getattr(paxlst_parser, segment.tag)
            self.assertEqual("ATT", cls().tag(segment))
            self.assertEqual(self.att1, cls().process(segment))

    def test_parser_att2(self):
        """Test parser output"""
        for segment in self.collection2.segments:
            cls = getattr(paxlst_parser, segment.tag)
            self.assertEqual("ATT", cls().tag(segment))
            self.assertEqual(self.att2, cls().process(segment))

    def tearDown(self):
        del self.collection1
        del self.att1
        del self.collection2
        del self.att2


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

        self.collection2 = Message.from_str("DTM+329:130414'")
        self.dtm2 = {
            'tag': "DTM",
            'element': {
                "329": {
                    "DATE_OF_BIRTH": "2014-04-13"
                }
            }
        }

        self.collection3 = Message.from_str("DTM+36:'")
        self.dtm3 = {
            'tag': "DTM",
            'element': {
                "36": {
                    "PASSPORT_EXPIRATION_DATE": None
                }
            }
        }

    def test_parser_dtm1(self):
        """Test parser output"""
        for segment in self.collection1.segments:
            cls = getattr(paxlst_parser, segment.tag)
            self.assertEqual("DTM", cls().tag(segment))
            self.assertEqual(self.dtm1, cls().process(segment))

    def test_parser_dtm2(self):
        """Test parser output"""
        for segment in self.collection2.segments:
            cls = getattr(paxlst_parser, segment.tag)
            self.assertEqual("DTM", cls().tag(segment))
            self.assertEqual(self.dtm2, cls().process(segment))

    def test_parser_dtm3(self):
        """Test parser output"""
        for segment in self.collection3.segments:
            cls = getattr(paxlst_parser, segment.tag)
            self.assertEqual("DTM", cls().tag(segment))
            self.assertEqual(self.dtm3, cls().process(segment))

    def tearDown(self):
        del self.collection1
        del self.dtm1
        del self.collection2
        del self.dtm2
        del self.collection3
        del self.dtm3
