import csv
import time

from config import *

from template import TemplateFaker


# TODO: redo the generator after reverting to functional code
class PnrGen(object):
    """generates passenger data"""

    def __init__(self, root_dir=None):
        if root_dir:
            self.root_dir = root_dir
        else:
            self.root_dir = str(ROOT_DIR)
        self.faker = TemplateFaker()

    def get_schema(self, schema):
        path = self.root_dir + '/schema/'
        data = []
        with open(os.path.join(path, schema)) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
        return data

    def generate(self, schema, size=10):
        items = self.get_schema(schema)
        records = []
        # run for all the datasets
        for i in range(0, size):
            record = self.faker.record(items)
            records.append(record)
        return records

    def save_data(self, records, filename):
        timestr = time.strftime("%Y-%m-%d")
        filename = filename.split('.')[0]
        filename = "%s_" % filename + timestr + ".csv"
        path = self.root_dir + '/data/'
        with open(os.path.join(path, filename), "a", newline="") as f:
            writer = csv.writer(f)
            record = records[0]
            header = dict(record).keys()
            # Write header
            if f.tell() == 0:
                writer.writerow(header)
            for record in records:
                writer.writerow(dict(record).values())
        print("Data generated.")


if __name__ == '__main__':
    schema = "./schema.csv"
    pnrgen = PnrGen()
    print(pnrgen.faker)
    print(pnrgen.generate(schema=schema, size=5))
