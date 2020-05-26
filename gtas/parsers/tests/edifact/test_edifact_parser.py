from django.test import TestCase
from pydifact.message import Message


class EdifactParserTest(TestCase):
    """Test for parsing an edifact message"""
    def setUp(self):
        self.edifacts = """UNB+UNOA:4+SAMPLE CARRIER NAME:ZZ+HDQCH2X:ZZ+200506:1700+123456789++PAXLST'
            UNH+53371718146010+PAXLST:D:02B:UN:IATA'
            BGM+745'
            NAD+MS+++WORLD CUSTOMS ORGANIZATION BRU'
            COM+17037919383:TE'
            TDT+20+YY123'
            LOC+125+IAD'
            DTM+189:2005061200:201'
            LOC+87+BRU'
            DTM+232:2005071322:201'
            NAD+FL+++ALI YYÉ'
            MEA+CT++1'
            MEA+WT++KGM:10'
            LOC+178+IAD'
            LOC+179+BRU'
            LOC+174+'
            RFF+AVF:ABC123'
            DOC++'
            DTM+36:'
            LOC+91+'
            NAD+FL+++EVELYN:AAKESSON'
            ATT+2++M'
            DTM+329:130414'
            LOC+174+SWE'
            NAT+2+SWE'
            RFF+AVF:89TVRV'
            RFF+SEA:16D'
            DOC+P+G839083'
            DTM+36:200101'
            LOC+91+SWE'
            NAD+FL+++IIDA:VILEN'
            ATT+2++M'
            DTM+329:321210'
            MEA+CT++2'
            MEA+WT++KGM:20'
            LOC+174+FIN'
            NAT+2+FIN'
            RFF+AVF:UQA8AC'
            RFF+SEA:61D'
            DOC+P+41570439'
            DTM+36:200102'
            LOC+91+FIN'
            NAD+FL+++JONUZ:MAJSTOROVIC'
            ATT+2++F'
            DTM+329:210906'
            LOC+174+SVN'
            NAT+2+SVN'
            RFF+AVF:17I57Q'
            RFF+SEA:78C'
            DOC+P+24416860'
            DTM+36:200103'
            LOC+91+SVN'
            NAD+FL+++KARI:SAEVARSSON'
            ATT+2++M'
            DTM+329:500522'
            MEA+CT++3'
            MEA+WT++KGM:30'
            LOC+174+ISL'
            NAT+2+ISL'
            RFF+AVF:17I57Q'
            RFF+SEA:10B'
            DOC+P+O1694677'
            DTM+36:200104'
            LOC+91+ISL'
            DTM+36:210101'
            NAD+FL+++LIBERA:MARCHESI'
            ATT+2++M'
            DTM+329:380822'
            LOC+174+ITA'
            NAT+2+ITA'
            RFF+AVF:P6PEPI'
            RFF+SEA:43D'
            DOC+P+M709842'
            DTM+36:200105'
            LOC+91+ITA'
            DTM+36:210102'
            NAD+FL+++MAX:VOGEL'
            ATT+2++M'
            DTM+329:900106'
            LOC+174+DEU'
            NAT+2+DEU'
            RFF+AVF:P3HPUN'
            RFF+SEA:79A'
            DOC+P+42878759'
            DTM+36:'
            LOC+91+DEU'
            DTM+36:210103'
            NAD+FL+++NUWWARRAH:WASEM'
            ATT+2++F'
            DTM+329:850822'
            LOC+174+EGY'
            NAT+2+EGY'
            RFF+AVF:P3HPUN'
            RFF+SEA:74B'
            DOC+P+F980648'
            DTM+36:'
            LOC+91+EGY'
            NAD+FL+++RAIMO:LAURILA'
            ATT+2++F'
            DTM+329:470822'
            LOC+174+FIN'
            NAT+2+FIN'
            RFF+AVF:HCTVT5'
            RFF+SEA:22G'
            DOC+P+11490614'
            DTM+36:'
            LOC+91+FIN'
            NAD+FL+++TOBIAS:DECKER'
            ATT+2++M'
            DTM+329:181203'
            LOC+174+DEU'
            NAT+2+DEU'
            RFF+AVF:HUJD8S'
            RFF+SEA:46E'
            DOC+P+X6091008'
            DTM+36:'
            LOC+91+DEU'
            CNT+42:10'
            UNT+23+53371718146010'
            UNZ+1+123456789'"""

    def test_edifact_parser(self):
        tags = []
        elements = []

        for edifact in self.edifacts.split("\n"):
            collection = Message.from_str(edifact)

            for segment in collection.segments:
                tags.append(segment.tag.strip())
                elements.append(segment.elements)
                # print('Segment tag: {}, content: {}'.format(segment.tag, segment.elements))

        self.assertEqual(tags[0], "UNB")
        self.assertEqual(elements[0], [['UNOA', '4'], ['SAMPLE CARRIER NAME', 'ZZ'], ['HDQCH2X', 'ZZ'], ['200506', '1700'], '123456789', '', 'PAXLST'])

        self.assertEqual(tags[1], "UNH")
        self.assertEqual(elements[1], ['53371718146010', ['PAXLST', 'D', '02B', 'UN', 'IATA']])

        self.assertEqual(tags[2], "BGM")
        self.assertEqual(elements[2], ['745'])

        self.assertEqual(tags[3], "NAD")
        self.assertEqual(elements[3], ['MS', '', '', 'WORLD CUSTOMS ORGANIZATION BRU'])

        self.assertEqual(tags[4], "COM")
        self.assertEqual(elements[4], [['17037919383', 'TE']])

        self.assertEqual(tags[5], "TDT")
        self.assertEqual(elements[5], ['20', 'YY123'])

    def tearDown(self):
        del self.edifacts
