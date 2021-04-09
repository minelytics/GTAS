from zipfile import ZipFile
import io
import csv

from config import *

DATA_SOURCE = str(ROOT_DIR) + '/source/' + 'pincode.zip'


class Address(object):
    def __init__(self):
        data_source = DATA_SOURCE
        self.records = dict()
        self.records['000000'] = {'city': 'Unknown', 'district': 'Unknown', 'state': 'Unknown'}
        with ZipFile(data_source) as zf:
            with zf.open('pincode.csv', 'r') as csvfile:
                reader = csv.DictReader(io.TextIOWrapper(csvfile, 'utf-8'))
                for dct in map(dict, reader):
                    self.records[dct['pincode']] = {'city': dct['taluk'], 'district': dct['district_name'],
                                                    'state': dct['state_name']}

    def get_state_code(self, state_name):
        state_codes = {
            '1': 'JAMMU AND KASHMIR',
            '2': 'HIMACHAL PRADESH',
            '3': 'PUNJAB',
            '4': 'CHANDIGARH',
            '5': 'UTTARAKHAND',
            '6': 'HARYANA',
            '7': 'DELHI',
            '8': 'RAJASTHAN',
            '9': 'UTTAR PRADESH',
            '10': 'BIHAR',
            '11': 'SIKKIM',
            '12': 'ARUNACHAL PRADESH',
            '13': 'NAGALAND',
            '14': 'MANIPUR',
            '15': 'MIZORAM',
            '16': 'TRIPURA',
            '17': 'MEGHALAYA',
            '18': 'ASSAM',
            '19': 'WEST BENGAL',
            '20': 'JHARKHAND',
            '21': 'ORISSA',
            '22': 'CHHATTISGARH',
            '23': 'MADHYA PRADESH',
            '24': 'GUJARAT',
            '25': 'DAMAN AND DIU',
            '26': 'DADAR AND NAGAR HAVELI',
            '27': 'MAHARASHTRA',
            '29': 'KARNATAKA',
            '30': 'GOA',
            '31': 'LAKSHADWEEP',
            '32': 'KERALA',
            '33': 'TAMIL NADU',
            '34': 'PUDUCHERRY',
            '35': 'ANDAMAN AND NICOBAR',
            '36': 'TELANGANA',
            '37': 'ANDHRA PRADESH',
            '38': 'LADAKH',
            '97': 'OTHER TERRITORY',
            '99': 'OTHER COUNTRY'
        }
        state_code = state_codes.get(state_name, "Invalid state")
        if isinstance(state_code, str):
            return "State Code Not Available"
        else:
            return state_code

    def get_state_alpha_code(self, address):
        address = address.strip()
        return address[-12:-10]

    def get_pincode(self, address):
        address = address.strip()
        return address[-9:-3]

    def get_city(self, address):
        pincode = self.get_pincode(address)
        # record = self.records[pincode]
        record = self.records.get(pincode, "Pincode Not Available")
        if isinstance(record, str):
            return "City Not Available"
        else:
            return record['city']
        # return record['city']

    def get_district(self, address):
        pincode = self.get_pincode(address)
        # record = self.records[pincode]
        record = self.records.get(pincode, "Pincode Not Available")
        if isinstance(record, str):
            return "District Not Available"
        else:
            return record['district']

    def get_state(self, address):
        pincode = self.get_pincode(address)
        record = self.records.get(pincode, "Pincode Not Available")
        if isinstance(record, str):
            return "State not available"
        else:
            # record = self.records[pincode]
            return record['state']


if __name__ == '__main__':
    address = Address()
    sample = "DONGAON,TAL DHARANGAON, DHARANGAON JALGAON (MH) IN 425103 JALGAON Jalgaon MH 425103 IN"
    print(address.get_pincode(sample))
    print(address.get_state_alpha_code(sample))
    print(address.get_city(sample))
    print(address.get_district(sample))
    print(address.get_state(sample))
