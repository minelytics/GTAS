import sys

from config import *

from faker import Faker
from collections import OrderedDict

from providers.choice import ChoiceProvider
from providers.country import CountryProvider
from providers.pattern import PatternProvider
from providers.pin import PinProvider
from providers.range import RangeProvider


class TemplateFaker(Faker):
    def __init__(self):
        Faker.__init__(self)
        # Add all providers
        self.add_provider(PatternProvider)
        self.add_provider(ChoiceProvider)
        self.add_provider(RangeProvider)
        self.add_provider(PinProvider)
        self.add_provider(CountryProvider)

    def record(self, schema_items):
        self.init()
        record = OrderedDict()
        for item in schema_items:
            if item['default_value']:
                record[item['field']] = item['default_value']
            else:
                if item['default_generator']:
                    generator = item['default_generator']
                else:
                    generator = item['generator']
                if generator == 'pattern':
                    record[item['field']] = self.pattern(item['value'])
                elif generator == 'choice':
                    record[item['field']] = self.choice(item['value'])
                elif generator == 'range':
                    record[item['field']] = self.range(item['value'], item['type'])
                elif generator == 'name':
                    record[item['field']] = self.person()
                elif generator == 'address':
                    record[item['field']] = self.address()
                elif generator == 'country':
                    record[item['field']] = self.country()
                elif generator == 'alpha2_code':
                    record[item['field']] = self.alpha2_code()
                elif generator == 'state':
                    record[item['field']] = self.state()
                elif generator == 'district':
                    record[item['field']] = self.district()
                elif generator == 'pin':
                    record[item['field']] = self.pin()
                elif generator == 'state_code':
                    record[item['field']] = self.state_code()
                else:
                    raise Exception("Invalid generator: " + generator)
                    # print(record) # debug
                    # records[item['id']] = record
                # print(records) # debug
        return record


if __name__ == '__main__':
    sys.exit("Please write a python module to provide schema in Orderdict to template provider")
