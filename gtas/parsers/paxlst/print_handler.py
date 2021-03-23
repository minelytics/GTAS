__author__ = "Chris Humphreys"
__version__ = "1.0.0"
__license__ = "GPL3"

import edifact as edifact
import json
import abc

class PrettyPrintHandler(edifact.Handler):

    def visit_codeset_element(self, data_element_schema, element, codeset_manager, codeset_code, verbose):
        codeset_value = codeset_manager.codeset_lookup(element, codeset_code)["name"]
        if 'desc' in data_element_schema:
             desc = data_element_schema['desc']
        else:
            desc = ""
        print("{} {}: '{}' ({})".format(data_element_schema["code"], desc, codeset_value, element))
        return False, None

    def visit_literal_element(self, data_element_schema, element, codeset_manager):
        if 'desc' in data_element_schema:
             desc = data_element_schema['desc']
        else:
            desc = ""
        print("{} {}: {}".format(data_element_schema["code"], desc, element))
        return False, None

    def visit_segment(self, segment, schema, schema_position):
        print("> ({})\n{}\n{}({}:{}) <".format(schema_position['code'], 
        schema_position['desc'], 
        schema['code'], 
        schema['conditional'], 
        schema['cardinality']))

    def visit_unknown_segment(self, segment):
        print('Segment tag: {}, content: {}'.format(segment.tag, segment.elements))

    def start(self):
        pass

    def end(self):
        pass

class JsonPrintHandler(edifact.Handler):
    def __init__(self):
        super().__init__()
        self._result = []
        self._current_segment = None

    def visit_codeset_element(self, data_element_schema, element, codeset_manager, codeset_code, verbose):
        codeset_value = codeset_manager.codeset_lookup(element, codeset_code)["name"]
        if 'desc' in data_element_schema:
             desc = data_element_schema['desc']
        else:
            desc = ""
        result = {
            "code" : data_element_schema["code"], 
            "name" : data_element_schema["name"],
            "desc" : desc, 
            "value" : codeset_value,
            "value_coded" : element
        }
        self._current_segment['attributes'].append(result)
        return False, None

    def visit_literal_element(self, data_element_schema, element, codeset_manager):
        if 'desc' in data_element_schema:
             desc = data_element_schema['desc']
        else:
            desc = ""
        result = {
            "code" : data_element_schema["code"], 
            "name" : data_element_schema["name"],
            "desc" : desc, 
            "value" : element
        }
        self._current_segment['attributes'].append(result)
        return False, None

    def visit_segment(self, segment, schema, schema_position):
        #print(schema_position['code'])
        current_group = self._result
        if '>' in schema_position['code']:
            parts = schema_position['code'].split('>')
            parts.reverse()
            parts = parts[0:-1]
            #print(f"Attempting to store {schema_position}")
            for part in parts:
                #print(f'checking part {part}')
                last_group = current_group[-1]
                last_group_code = last_group['code']
                #print(f"last group: {last_group_code}")
                if part == last_group_code:
                    group = last_group
                    #print(f"using last group {last_group_code}")
                else:
                    group = {
                        "code" : part,
                        "segments" : []
                    }
                    #print(f'creating group {part}')
                    current_group.append(group)
                current_group = group['segments']

        self._current_segment = {     
            "hierarchy" : schema_position['code'],
            "desc" : schema_position['desc'], 
            "code" : schema['code'], 
            "conditional" : schema['conditional'], 
            "cardinality" : schema['cardinality'],
            "attributes" : []
        }
        current_group.append(self._current_segment)


    def visit_unknown_segment(self, segment):
        self._current_segment = {     
            "code" : segment.tag,
            "attributes" : []
        }
        self._result.append(self._current_segment)
        for element in segment.elements:
            self._visit_unknown_element(element)

    def _visit_unknown_element(self, element):
        result = {
            "code" : element['code'],
            "value" : element['value']

        }
        self._current_segment['attributes'].append(result)

    def start(self):
        self._result = []

    def end(self):
        print(json.dumps(self._result))
        pass

