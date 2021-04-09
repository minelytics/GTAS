from faker import Faker
from faker.providers import BaseProvider

from xeger import Xeger


class PatternProvider(BaseProvider):

    def pattern(self, exp, limit=10):
        x = Xeger(limit=10)
        return x.xeger(exp)


if __name__ == '__main__':
    faker = Faker()
    faker.add_provider(PatternProvider)
    print(faker.pattern("^[0-9]{2}[A-Z]{5}([0-9]){4}([A-Z]){1}?[0-9]Z[0-9]$"))
