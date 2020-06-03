from django.test import TestCase

from gtas.generator.workflow.api.edifact_generator import EdifactGenerator


class EdifactGeneratorTest(TestCase):
    """Test for edifact parser"""

    def test_single_segment_output(self):
        messages = []
        generator = EdifactGenerator()

        messages.append(generator.generate_edifact('UNB', [['UNOA', '4'], ['SAMPLE CARRIER NAME', 'ZZ'], ['HDQCH2X', 'ZZ'], ['200506', '1700'], '123456789', '', 'PAXLST']))
        messages.append(generator.generate_edifact('UNH', ['53371718146010', ['PAXLST', 'D', '02B', 'UN', 'IATA']]))
        messages.append(generator.generate_edifact('BGM', ['745']))
        messages.append(generator.generate_edifact('NAD', ['MS', '', '', 'WORLD CUSTOMS ORGANIZATION BRU']))

        self.assertEqual(messages[0], "UNB+UNOA:4+SAMPLE CARRIER NAME:ZZ+HDQCH2X:ZZ+200506:1700+123456789++PAXLST'")
        self.assertEqual(messages[1], "UNH+53371718146010+PAXLST:D:02B:UN:IATA'")
        self.assertEqual(messages[2], "BGM+745'")
        self.assertEqual(messages[3], "NAD+MS+++WORLD CUSTOMS ORGANIZATION BRU'")
