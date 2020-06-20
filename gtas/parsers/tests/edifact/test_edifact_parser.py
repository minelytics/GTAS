from django.conf import settings
from django.test import TestCase

from gtas.parsers.edifact.edifact_parser import EdifactParser, TagsElementsParser


class EdifactParserTest(TestCase):
    """Test for edifact parser"""
    def setUp(self):
        edifact_parser = EdifactParser()
        file = str(settings.APPS_DIR) + "/parsers/tests/resources/sample-edifact-messages/text_001.txt"
        self.parsed_message = edifact_parser.get_parsed_message(file)

    def test_tags_and_elements_for_loc(self):
        tags_elements_parser = TagsElementsParser()
        output = tags_elements_parser.parsed_output(self.parsed_message)

        for data in output:
            if data["tag"] == "LOC":
                self.assertEqual(data["tag"], "LOC")

                for elements in data["elements"]:
                    for key, value in elements.items():
                        self.assertEqual(elements[key], value)
