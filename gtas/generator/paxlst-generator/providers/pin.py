from zipfile import ZipFile
import io
import csv

from faker import Faker
from faker.providers import BaseProvider

from config import *

DATA_SOURCE = str(ROOT_DIR) + '/source/' + 'pincode.zip'
file_path = str(ROOT_DIR) + '/source/' + 'state_code.zip'


class PinProvider(BaseProvider):
    init_done = False

    def init(self):
        if not self.init_done:
            data_source = DATA_SOURCE
            self.pins = []
            self.states = []
            self.districts = []
            self.taluks = []
            self.records = []
            self.code = {}
            with ZipFile(data_source) as zf:
                with zf.open('pincode.csv', 'r') as csvfile:
                    reader = csv.DictReader(io.TextIOWrapper(csvfile, 'utf-8'))
                    for dct in map(dict, reader):
                        self.records.append(dct)

            # code for the state code
            with ZipFile(file_path) as zf:
                with zf.open('state_code.csv', 'r') as csvfile:
                    reader = csv.DictReader(io.TextIOWrapper(csvfile, 'utf-8'))
                    for row in reader:
                        key = row.pop('state_name')
                        if key in self.code:
                            # implement your duplicate row handling here
                            pass
                        self.code[key] = row['code']

            for record in self.records:
                self.pins.append(record['pincode'])
                self.states.append(record['state_name'])
                self.districts.append(record['district_name'])
                self.taluks.append(record['taluk'])

            # TODO Deduplicate the states, districts, taluks using python calls
            self.init_done = True

    def pin(self):
        self.init()
        return self.random_element(self.pins)

    def pins(self, length):
        self.init()
        return self.random_elements(self.pins, length)

    def state(self):
        self.init()
        return self.random_element(self.states)

    def states(self, length):
        self.init()
        return self.random_elements(self.states, length)

    def district(self):
        self.init()
        return self.random_element(self.districts)

    def districts(self, length):
        self.init()
        return self.random_elements(self.districts, length)

    def taluk(self):
        self.init()
        return self.random_element(self.taluks)

    def taluks(self, length):
        self.init()
        return self.random_elements(self.taluks, length)

    def pin_record(self):
        self.init()
        return self.random_element(self.records)

    def pin_records(self, length):
        self.init()
        return self.random_elements(self.records, length)

    def state_code(self):
        self.init()
        state = self.random_element(self.states)
        if state in self.code:
            return self.code[state]
        else:
            return "99"


if __name__ == '__main__':
    faker = Faker()
    faker.add_provider(PinProvider)
    print(faker.pin())
    print(faker.state())
    print(faker.state_code())
    print(faker.district())
    print(faker.taluk())
    print(faker.pin_record())
    print(faker.pins(10))
    print(faker.states(10))
    print(faker.districts(10))
    print(faker.taluks(10))
    print(faker.pin_records(10))
    print(faker.state_code())
