__author__ = "Chris Humphreys"
__version__ = "1.0.0"
__license__ = "GPL3"

import unittest
from schema import SchemaTraverser, load_schema

class TestParse(unittest.TestCase):

    def test_traverse_all_segment_codes_no_groups_no_loop(self):
        cuscar_schema = load_schema("schema_for_test.json")
        traverser = SchemaTraverser(cuscar_schema)

        all_segment_codes = [i['code'] for i in traverser.segment_generator(follow_loops = False)]
        expected = ['UNA', 'UNB', 'BGM', 'DTM', 'UNT', 'UNZ']
        self.assertEqual(all_segment_codes, expected)

    def test_traverse_all_segment_codes_no_groups_with_loop(self):
        cuscar_schema = load_schema("schema_for_test.json")
        traverser = SchemaTraverser(cuscar_schema)

        all_segment_codes = [i['code'] for i in traverser.segment_generator(follow_loops = True)]
        expected = ['UNA', 'UNB', 'BGM', 'DTM', 'DTM', 'DTM', 'DTM', 'DTM', 'DTM', 'DTM', 'DTM', 'DTM', 'UNT', 'UNZ']
        self.assertEqual(all_segment_codes, expected)

    def test_traverse_all_segment_codes_with_groups_no_loops(self):
        cuscar_schema = load_schema("schema_for_test2.json")
        traverser = SchemaTraverser(cuscar_schema)

        all_segment_codes = [i['code'] for i in traverser.segment_generator(follow_loops = False)]
        expected = ['UNA', 'UNB', 'AUT', 'DTM', 'RFF', 'UNT', 'UNZ']
        self.assertEqual(all_segment_codes, expected)

    def test_traverse_all_segment_codes_with_groups_and_loops(self):
        cuscar_schema = load_schema("schema_for_test2.json")
        traverser = SchemaTraverser(cuscar_schema)

        all_segment_codes = [i['code'] for i in traverser.segment_generator(follow_loops=True)]

        expected = ['UNA', 'UNB', 'AUT', 
            'DTM', 'DTM', 'DTM', 'DTM', 'DTM', 'DTM', 'DTM', 'DTM', 'DTM',
            'RFF', 'RFF', 'RFF', 'RFF', 'RFF', 'RFF', 'RFF', 'RFF', 'RFF', 
            'UNT', 'UNZ']
        self.assertEqual(all_segment_codes, expected)


    def test_can_find_forward_by_segment_code_no_repeating(self):
        cuscar_schema = load_schema("schema_for_test.json")
        traverser = SchemaTraverser(cuscar_schema)

        self.assertEqual(traverser.find_segment_forward('UNB')[0]['code'], 'UNB') 
        self.assertEqual(traverser.find_segment_forward('BGM')[0]['code'], 'BGM')
        self.assertEqual(traverser.find_segment_forward('DTM')[0]['code'], 'DTM')
        self.assertEqual(traverser.find_segment_forward('UNT')[0]['code'], 'UNT')

    def test_can_find_forward_by_segment_code_repeating_segments(self):
        cuscar_schema = load_schema("schema_for_test.json")
        traverser = SchemaTraverser(cuscar_schema)

        self.assertEqual(traverser.find_segment_forward('UNB')[0]['code'], 'UNB')
        self.assertEqual(traverser.find_segment_forward('BGM')[0]['code'], 'BGM')
        self.assertEqual(traverser.find_segment_forward('DTM')[0]['code'], 'DTM')
        self.assertEqual(traverser.find_segment_forward('DTM')[0]['code'], 'DTM')
        self.assertEqual(traverser.find_segment_forward('DTM')[0]['code'], 'DTM')
        self.assertEqual(traverser.find_segment_forward('DTM')[0]['code'], 'DTM')
        self.assertEqual(traverser.find_segment_forward('DTM')[0]['code'], 'DTM')
        self.assertEqual(traverser.find_segment_forward('DTM')[0]['code'], 'DTM')
        self.assertEqual(traverser.find_segment_forward('DTM')[0]['code'], 'DTM')
        self.assertEqual(traverser.find_segment_forward('DTM')[0]['code'], 'DTM')
        self.assertEqual(traverser.find_segment_forward('DTM')[0]['code'], 'DTM')
        self.assertEqual(traverser.find_segment_forward('UNT')[0]['code'], 'UNT')
        
    def test_will_fail_if_cannot_find_segment(self):
        cuscar_schema = load_schema("schema_for_test.json")
        traverser = SchemaTraverser(cuscar_schema)

        self.assertEqual(traverser.find_segment_forward('UNB')[0]['code'], 'UNB')
        with self.assertRaises(Exception) as context:
            traverser.find_segment_forward('XXX')

        self.assertTrue('Segment not found XXX' in str(context.exception))

    def test_will_fail_if_cannot_find_repeated_segment_too_any_times(self):
        cuscar_schema = load_schema("schema_for_test.json")
        traverser = SchemaTraverser(cuscar_schema)

        self.assertEqual(traverser.find_segment_forward('UNB')[0]['code'], 'UNB')
        self.assertEqual(traverser.find_segment_forward('BGM')[0]['code'], 'BGM')
        self.assertEqual(traverser.find_segment_forward('DTM')[0]['code'], 'DTM')
        self.assertEqual(traverser.find_segment_forward('DTM')[0]['code'], 'DTM')
        self.assertEqual(traverser.find_segment_forward('DTM')[0]['code'], 'DTM')
        self.assertEqual(traverser.find_segment_forward('DTM')[0]['code'], 'DTM')
        self.assertEqual(traverser.find_segment_forward('DTM')[0]['code'], 'DTM')
        self.assertEqual(traverser.find_segment_forward('DTM')[0]['code'], 'DTM')
        self.assertEqual(traverser.find_segment_forward('DTM')[0]['code'], 'DTM')
        self.assertEqual(traverser.find_segment_forward('DTM')[0]['code'], 'DTM')
        self.assertEqual(traverser.find_segment_forward('DTM')[0]['code'], 'DTM')
        
        with self.assertRaises(Exception) as context:
            traverser.find_segment_forward('DTM')

        self.assertTrue('Segment not found DTM' in str(context.exception))



if __name__ == '__main__':
    unittest.main()
