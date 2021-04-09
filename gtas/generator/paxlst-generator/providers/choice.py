from faker import Faker
from faker.providers import BaseProvider


class ChoiceProvider(BaseProvider):
    def choice(self, value):
        elements = value.split(",")
        return self.random_element(elements)


if __name__ == "__main__":
    faker = Faker()
    faker.add_provider(ChoiceProvider)
    print(faker.choice("0,5,18,22"))
