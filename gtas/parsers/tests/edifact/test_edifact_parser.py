from django.test import TestCase
from pydifact.message import Message


class EdifactParserTest(TestCase):
    """Test for parsing an edifact message"""
    def setUp(self):
        self.edifacts1 = """UNB+UNOA:4+SAMPLE CARRIER NAME:ZZ+HDQCH2X:ZZ+200506:1700+123456789++PAXLST'
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
        self.edifacts2 = """UNA:+.? '
            UNB+UNOA:4+APIS*ABE+USADHS+070429:0900+000000001++USADHS'
            UNG+PAXLST+XYZ AIRLINES+USADHS+070429:0900+100+UN+D:05B'
            UNH+PAX001+PAXLST:D:05B:UN:IATA+API01+01'
            BGM+745'
            RFF+TN:BA123456789:::1'
            NAD+MS+++JACKSON'
            COM+703-555-1234:TE+703-555-9876:FX'
            TDT+20+UA123+++UA'
            LOC+125+YVR'
            DTM+189:0704291230:201'
            LOC+87+JFK'
            DTM+232:0704291600:201'
            TDT+20+UA124+++UA'
            LOC+92+JFK'
            DTM+189:0704291730:201'
            LOC+92+ATL'
            DTM+232:0704291945:201'
            NAD+FL+++DOE:JOHN:WAYNE+20 MAIN ST+ANYCITY+VA+10053+USA'
            ATT+2++M'
            DTM+329:570121'
            FTX+BAG+++UA123456:3'
            LOC+22+JFK'
            LOC+178+YVR'
            LOC+179+ATL'
            LOC+174+CAN'
            COM+502-555-1234:TE'
            NAT+2+CAN'
            RFF+AVF:ABC123'
            RFF+ABO:BA1321654987'
            RFF+AEA:1234567890ABC'
            RFF+CR:20060907NY123'
            RFF+SEA:23C'
            DOC+P:110:111+MB140241'
            DTM+36:081021'
            LOC+91+CAN'
            CNT+42:1'
            UNT+35+PAX001'
            UNE+1+100'
            UNZ+1+000000001'"""

    def test_edifact_parser(self):
        tags = []
        elements = []

        for edifact in self.edifacts1.split("\n"):
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

    def test_edifact_parser2(self):
        tags = []
        elements = []

        for edifact in self.edifacts2.split("\n"):
            collection = Message.from_str(edifact)

            for segment in collection.segments:
                tags.append(segment.tag.strip())
                elements.append(segment.elements)
                # print('Segment tag: {}, content: {}'.format(segment.tag, segment.elements))

        self.assertEqual(tags[0], "UNA")
        self.assertEqual(elements[0], [":+.? '"])

        self.assertEqual(tags[1], "UNB")
        self.assertEqual(elements[1], [['UNOA', '4'], 'APIS*ABE', 'USADHS', ['070429', '0900'], '000000001', '', 'USADHS'])

        self.assertEqual(tags[2], "UNG")
        self.assertEqual(elements[2], ['PAXLST', 'XYZ AIRLINES', 'USADHS', ['070429', '0900'], '100', 'UN', ['D', '05B']])

        self.assertEqual(tags[3], "UNH")
        self.assertEqual(elements[3], ['PAX001', ['PAXLST', 'D', '05B', 'UN', 'IATA'], 'API01', '01'])

        self.assertEqual(tags[4], "BGM")
        self.assertEqual(elements[4], ['745'])

        self.assertEqual(tags[5], "RFF")
        self.assertEqual(elements[5], [['TN', 'BA123456789', '', '', '1']])

    def tearDown(self):
        del self.edifacts1
        del self.edifacts2
