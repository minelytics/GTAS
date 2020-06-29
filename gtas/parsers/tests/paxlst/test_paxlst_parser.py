from django.test import TestCase
from pydifact import Message

from gtas.parsers.paxlst.paxlst_parser import PaxlstParser


class BaseTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Added this class from https://gist.github.com/twolfson/13f5f5784f67fd49b245
        Useful for inheriting setUp() variables

        cls_atomics error solution link
        https://stackoverflow.com/questions/29653129/update-to-django-1-8-attributeerror-django-test-testcase-has-no-attribute-cl
        """
        if cls is not BaseTestCase and cls.setUp is not BaseTestCase.setUp:
            orig_setUp = cls.setUp

            def setUpOverride(self, *args, **kwargs):
                BaseTestCase.setUp(self)
                return orig_setUp(self, *args, **kwargs)

            cls.setUp = setUpOverride
        super(BaseTestCase, cls).setUpClass()

    def setUp(self):
        self.collections = []
        self.outputs = []

    def expected_structure(self, tag, sub_element, key, value):
        return {
            'tag': tag,
            'element': {
                sub_element: {
                    key: value
                }
            }
        }

    def parser_test(self, tag, collections, outputs):
        for collection, output in zip(collections, outputs):
            for segment in collection.segments:
                cls = getattr(PaxlstParser().get_segment(segment.tag), segment.tag)
                self.assertEqual(tag, cls().tag(segment))
                self.assertEqual(output, cls().process(segment))

    def tearDown(self):
        del self.collections
        del self.outputs


class ATTTest(BaseTestCase):
    """Test for ATT Tag"""
    def setUp(self):
        self.collections.append(Message.from_str("ATT+2++M'"))
        self.outputs.append(self.expected_structure("ATT", "2", "GENDER", "M"))

        self.collections.append(Message.from_str("ATT+2++F'"))
        self.outputs.append(self.expected_structure("ATT", "2", "GENDER", "F"))

    def test_parser_att(self):
        self.parser_test("ATT", self.collections, self.outputs)

    def tearDown(self):
        self.collections.clear()
        self.outputs.clear()


class BGMTest(BaseTestCase):
    """Test for BGM Tag"""
    def setUp(self):
        self.collections.append(Message.from_str("BGM+745'"))
        self.outputs.append(self.expected_structure("BGM", "745", "PASSENGER_LIST", "No Document Identifier used"))

        self.collections.append(Message.from_str("BGM+745+CP'"))
        self.outputs.append(self.expected_structure("BGM", "745", "PASSENGER_LIST", "CHANGE_PAX_DATA"))

        self.collections.append(Message.from_str("BGM+266+CLOB'"))
        self.outputs.append(self.expected_structure("BGM", "266", "FLIGHT_STATUS_UPDATE", "FLIGHT_CLOSE_WITH_PAX_ON_BOARD"))

    def test_parser_bgm(self):
        self.parser_test("BGM", self.collections, self.outputs)

    def tearDown(self):
        self.collections.clear()
        self.outputs.clear()


class CNTTest(BaseTestCase):
    """Test for CNT Tag"""
    def setUp(self):
        self.collections.append(Message.from_str("CNT+42:10'"))
        self.outputs.append(self.expected_structure("CNT", "42", "TOTAL_CREW_MEMBERS", "10"))

        self.collections.append(Message.from_str("CNT+41:12'"))
        self.outputs.append(self.expected_structure("CNT", "41", "TOTAL_PASSENGERS", "12"))

    def test_parser_cnt(self):
        self.parser_test("CNT", self.collections, self.outputs)

    def tearDown(self):
        self.collections.clear()
        self.outputs.clear()


class COMTest(BaseTestCase):
    """Test for COM Tag"""
    def setUp(self):
        self.collections.append(Message.from_str("COM+17037919383:TE'"))
        self.outputs.append(self.expected_structure("COM", "TE", "TELEPHONE", "17037919383"))

        self.collections.append(Message.from_str("COM+703 555 1234:TE+703 555 9876:FX'"))
        self.com1 = self.expected_structure("COM", "TE", "TELEPHONE", "703 555 1234")
        self.com1["element"].update({"FX":{"TELEFAX": "703 555 9876"}})
        self.outputs.append(self.com1)

    def test_parser_com(self):
        self.parser_test("COM", self.collections, self.outputs)

    def tearDown(self):
        self.collections.clear()
        self.outputs.clear()
        del self.com1


class DOCTest(BaseTestCase):
    """Test for DOC Tag"""
    def setUp(self):
        self.collections.append(Message.from_str("DOC+P+G839083'"))
        self.outputs.append(self.expected_structure("DOC", "P", "PASSPORT", "G839083"))

        self.collections.append(Message.from_str("DOC++'"))
        self.outputs.append(self.expected_structure("DOC", "", "DOC Unknown Code List Identification Code: ", ""))

        self.collections.append(Message.from_str("DOC+P:110:111+MB140241'"))
        self.doc1 = self.expected_structure("DOC", "P", "PASSPORT", "MB140241")
        self.doc1["element"]["P"].update({"IDENTIFICATION_CODE": "US_DHS_SPECIAL_CODES"})
        self.doc1["element"]["P"].update({"RESPONSIBLE_AGENCY_CODE": "US_DEPARTMENT_OF_HOMELAND_SECURITY"})
        self.outputs.append(self.doc1)

    def test_parser_doc(self):
        self.parser_test("DOC", self.collections, self.outputs)

    def tearDown(self):
        self.collections.clear()
        self.outputs.clear()
        del self.doc1


class DTMTest(BaseTestCase):
    """Test for DTM Tag"""
    def setUp(self):
        self.collections.append(Message.from_str("DTM+189:2005061200:201'"))
        self.outputs.append(self.expected_structure("DTM", "189", "DEPARTURE_DATETIME", "2020-05-06 12:00"))

        self.collections.append(Message.from_str("DTM+329:130414'"))
        self.outputs.append(self.expected_structure("DTM", "329", "DATE_OF_BIRTH", "2014-04-13"))

        self.collections.append(Message.from_str("DTM+36:'"))
        self.outputs.append(self.expected_structure("DTM", "36", "PASSPORT_EXPIRATION_DATE", None))

    def test_parser_dtm(self):
        self.parser_test("DTM", self.collections, self.outputs)

    def tearDown(self):
        self.collections.clear()
        self.outputs.clear()


class LOCTest(BaseTestCase):
    """Test for LOC Tag"""
    def setUp(self):
        self.collections.append(Message.from_str("LOC+125+IAD'"))
        self.outputs.append(self.expected_structure("LOC", "125", "DEPARTURE_AIRPORT", "IAD"))

        self.collections.append(Message.from_str("LOC+87+BRU'"))
        self.outputs.append(self.expected_structure("LOC", "87", "ARRIVAL_AIRPORT", "BRU"))

    def test_parser_loc(self):
        self.parser_test("LOC", self.collections, self.outputs)

    def tearDown(self):
        self.collections.clear()
        self.outputs.clear()


class NADTest(BaseTestCase):
    """Test for NAD Tag"""
    def setUp(self):
        self.collections.append(Message.from_str("NAD+MS+++WORLD CUSTOMS ORGANIZATION BRU'"))
        self.outputs.append(self.expected_structure("NAD", "MS", "REPORTING_PARTY", "WORLD CUSTOMS ORGANIZATION BRU"))

        self.collections.append(Message.from_str("NAD+FL+++DOE:JOHN:WAYNE+20 MAIN STREET+ANYCITY+VA+10053+USA'"))
        self.nad1 = self.expected_structure("NAD", "FL", "PASSENGER", "JOHN WAYNE DOE")
        self.nad1["element"].update({
            "ADDRESS":{
                "NAME_AND_STREET_IDENTIFIER": "20 MAIN STREET",
                "CITY": "ANYCITY",
                "COUNTRY_SUB_CODE": "VA",
                "POSTAL_CODE": "10053",
                "COUNTRY_CODE": "USA"
            }
        })
        self.outputs.append(self.nad1)

        self.collections.append(Message.from_str(""))
        self.outputs.append(self.expected_structure("NAD", "MS", "REPORTING_PARTY", "WORLD CUSTOMS ORGANIZATION BRU"))

    def test_parser_nad(self):
        self.parser_test("NAD", self.collections, self.outputs)

    def tearDown(self):
        self.collections.clear()
        self.outputs.clear()
        del self.nad1


class NATTest(BaseTestCase):
    """Test for NAT Tag"""
    def setUp(self):
        self.collections.append(Message.from_str("NAT+2+SWE'"))
        self.outputs.append(self.expected_structure("NAT", "2", "NATIONALITY_NAME_CODE", "SWE"))

        self.collections.append(Message.from_str("NAT+2+SVN'"))
        self.outputs.append(self.expected_structure("NAT", "2", "NATIONALITY_NAME_CODE", "SVN"))

    def test_parser_nat(self):
        self.parser_test("NAT", self.collections, self.outputs)

    def tearDown(self):
        self.collections.clear()
        self.outputs.clear()


class RFFTest(BaseTestCase):
    """Test for RFF Tag"""
    def setUp(self):
        self.collections.append(Message.from_str("RFF+AVF:ABC123'"))
        self.outputs.append(self.expected_structure("RFF", "AVF", "PASSENGER_RESERVATION_NUMBER", "ABC123"))

        self.collections.append(Message.from_str("RFF+SEA:78C'"))
        self.outputs.append(self.expected_structure("RFF", "SEA", "SEAT_NUMBER", "78C"))

    def test_parser_rff(self):
        self.parser_test("RFF", self.collections, self.outputs)

    def tearDown(self):
        self.collections.clear()
        self.outputs.clear()


class TDTTest(BaseTestCase):
    """Test for TDT Tag"""
    def setUp(self):
        self.collections.append(Message.from_str("TDT+20+YY123'"))
        self.outputs.append(self.expected_structure("TDT", "20", "ARRIVING_OR_DEPARTING_FLIGHT", "YY123"))

        self.collections.append(Message.from_str("TDT+20+UA123+++UA'"))
        self.tdt1 = self.expected_structure("TDT", "20", "ARRIVING_OR_DEPARTING_FLIGHT", "UA123")
        self.tdt1["element"].update({"CARRIER_IDENTIFIER": "UA"})
        self.outputs.append(self.tdt1)

    def test_parser_tdt(self):
        self.parser_test("TDT", self.collections, self.outputs)

    def tearDown(self):
        self.collections.clear()
        self.outputs.clear()
