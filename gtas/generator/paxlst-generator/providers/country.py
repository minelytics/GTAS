from zipfile import ZipFile
import io
import csv

from faker import Faker
from faker.providers import BaseProvider

from config import *

DATA_SOURCE = str(ROOT_DIR) + "/source/" + "country.zip"


class CountryProvider(BaseProvider):
    init_done = False

    def init(self):
        if not self.init_done:
            data_source = DATA_SOURCE
            self.country = []
            self.french = []
            self.alpha2_code = []
            self.alpha3_code = []
            self.numeric = []
            self.records = []
            with ZipFile(data_source) as zf:
                with zf.open("country.csv", "r") as csvfile:
                    reader = csv.DictReader(io.TextIOWrapper(csvfile, "utf-8"))
                    for dct in map(dict, reader):
                        self.records.append(dct)

            for record in self.records:
                self.country.append(record["country"])
                self.french.append(record["french"])
                self.alpha2_code.append(record["alpha2_code"])
                self.alpha3_code.append(record["alpha3_code"])
                self.numeric.append(record["numeric"])

            # TODO Deduplicate the states, districts, taluks using python calls
            self.init_done = True

    def country(self):
        self.init()
        return self.random_element(self.country)

    def french(self):
        self.init()
        return self.random_element(self.french)

    def alpha2_code(self):
        self.init()
        return self.random_element(self.alpha2_code)

    def alpha3_code(self):
        self.init()
        return self.random_element(self.alpha3_code)

    def numeric(self):
        self.init()
        return self.random_element(self.numeric)


if __name__ == "__main__":
    faker = Faker()
    faker.add_provider(CountryProvider)
    print(faker.country())
    print(faker.french())
    print(faker.alpha2_code())
    print(faker.alpha3_code())
    print(faker.numeric())
