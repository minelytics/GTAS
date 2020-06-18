from django.test import TestCase
from pydifact import Message

from gtas.parsers.paxlst import paxlst_parser


class BaseTest(TestCase):
    def expected(self, tag, sub_element, key, value):
        return {
            'tag': tag,
            'element': {
                sub_element: {
                    key: value
                }
            }
        }


class ATTTest(BaseTest):
    """Test for ATT Tag"""
    def setUp(self):
        """Pydifact parsed message"""
        self.collection1 = Message.from_str("ATT+2++M'")
        self.att1 = self.expected("ATT", "2", "GENDER", "M")

        self.collection2 = Message.from_str("ATT+2++F'")
        self.att2 = self.expected("ATT", "2", "GENDER", "F")

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


class BGMTest(BaseTest):
    """Test for BGM Tag"""
    def setUp(self):
        """Pydifact parsed message"""
        self.collection1 = Message.from_str("BGM+745'")
        self.bgm1 = self.expected("BGM", "745", "PASSENGER_LIST", "No Document Identifier used")

        self.collection2 = Message.from_str("BGM+745+CP'")
        self.bgm2 = self.expected("BGM", "745", "PASSENGER_LIST", "CHANGE_PAX_DATA")

        self.collection3 = Message.from_str("BGM+266+CLOB'")
        self.bgm3 = self.expected("BGM", "266", "FLIGHT_STATUS_UPDATE", "FLIGHT_CLOSE_WITH_PAX_ON_BOARD")

    def test_parser_bgm1(self):
        """Test parser output"""
        for segment in self.collection1.segments:
            cls = getattr(paxlst_parser, segment.tag)
            self.assertEqual("BGM", cls().tag(segment))
            self.assertEqual(self.bgm1, cls().process(segment))

    def test_parser_bgm2(self):
        """Test parser output"""
        for segment in self.collection2.segments:
            cls = getattr(paxlst_parser, segment.tag)
            self.assertEqual("BGM", cls().tag(segment))
            self.assertEqual(self.bgm2, cls().process(segment))

    def test_parser_bgm3(self):
        """Test parser output"""
        for segment in self.collection3.segments:
            cls = getattr(paxlst_parser, segment.tag)
            self.assertEqual("BGM", cls().tag(segment))
            self.assertEqual(self.bgm3, cls().process(segment))

    def tearDown(self):
        del self.collection1
        del self.bgm1
        del self.collection2
        del self.bgm2
        del self.collection3
        del self.bgm3


# class CNTTest(TestCase):
#     """Test for CNT Tag"""
#     def setUp(self):
#         """Pydifact parsed message"""
#         self.collection1 = Message.from_str()


class DTMTest(BaseTest):
    """Test for DTM Tag"""
    def setUp(self):
        self.collection1 = Message.from_str("DTM+189:2005061200:201'")
        self.dtm1 = self.expected("DTM", "189", "DEPARTURE_DATETIME", "2020-05-06 12:00")

        self.collection2 = Message.from_str("DTM+329:130414'")
        self.dtm2 = self.expected("DTM", "329", "DATE_OF_BIRTH", "2014-04-13")

        self.collection3 = Message.from_str("DTM+36:'")
        self.dtm3 = self.expected("DTM", "36", "PASSPORT_EXPIRATION_DATE", None)

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


class LOCTest(BaseTest):
    """Test for LOC Tag"""
    def setUp(self):
        """Pydifact parsed message"""
        self.collection1 = Message.from_str("LOC+125+IAD'")
        self.loc1 = self.expected("LOC", "125", "DEPARTURE_AIRPORT", "IAD")

        self.collection2 = Message.from_str("LOC+87+BRU'")
        self.loc2 = self.expected("LOC", "87", "ARRIVAL_AIRPORT", "BRU")

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
