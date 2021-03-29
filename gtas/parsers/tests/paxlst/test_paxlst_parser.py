import pytest


@pytest.fixture
def fuction_fixture():
    print("Fixture for each test")
    return 1


@pytest.fixture(scope="module")
def module_fixture():
    print("Fixture for module")
    return 2
