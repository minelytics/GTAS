from faker import Faker
from faker.providers.date_time import Provider as DatetimeProvider
import random
from datetime import datetime


class RangeProvider(DatetimeProvider):
    def range(self, value, value_type='integer'):
        range_values = value.split(':')
        if value_type == 'keyword':
            min = int(range_values[0])
            max = int(range_values[1])
            return str(self.random_int(min=min, max=max))
        elif value_type == 'text':
            min = int(range_values[0])
            max = int(range_values[1])
            return str(self.random_int(min=min, max=max))
        elif value_type == 'integer':
            min = int(range_values[0])
            max = int(range_values[1])
            return str(self.random_int(min=min, max=max))
        elif value_type == 'double':
            min = float(range_values[0])
            max = float(range_values[1])
            # TODO change the round to faker method
            return round(random.uniform(min, max), 2)
        elif value_type == 'date':
            start = datetime.strptime(range_values[0], "%Y/%m/%d")
            end = datetime.strptime(range_values[1], "%Y/%m/%d")
            return self.date_between_dates(date_start=start, date_end=end)
        else:
            raise Exception("Invalid value type" + value)


if __name__ == '__main__':
    faker = Faker()
    faker.add_provider(RangeProvider)
    print(faker.range("0:22"))
    print(faker.range("2019/01/01:2019/12/01", 'date'))
