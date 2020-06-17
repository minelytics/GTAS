from django.test import TestCase
from pydifact import Message

from gtas.parsers.edifact import parser


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
            cls = getattr(parser, segment.tag)
            self.assertEqual("LOC", cls().tag(segment))
            self.assertEqual(self.loc1, cls().process(segment))

    def test_parser_loc2(self):
        """Test the parser output"""
        for segment in self.collection2.segments:
            cls = getattr(parser, segment.tag)
            self.assertEqual("LOC", cls().tag(segment))
            self.assertEqual(self.loc2, cls().process(segment))
