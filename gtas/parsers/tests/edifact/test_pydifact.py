from django.test import TestCase
import sys

class PydifactTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pydifact_load(self):
        import pydifact
        if 'pydifact' in sys.modules:
            status = True
        else:
            status = False
        self.assertEqual(status, True)

