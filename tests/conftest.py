import pytest

from tests.fixtures.base_fixtures import create_and_delete_resource, create_resource
from tests.fixtures.payment_fixture import TestPaymentCardAPIControllerFixture
from tests.fixtures.user_fixtures import TestUserAPIControllerFixture


# Payment
@pytest.fixture
def create_and_delete_test_payment():
    yield from create_and_delete_resource(TestPaymentCardAPIControllerFixture)


@pytest.fixture
def create_test_payment():
    yield from create_resource(TestPaymentCardAPIControllerFixture)


# User
@pytest.fixture
def create_and_delete_test_user():
    yield from create_and_delete_resource(TestUserAPIControllerFixture)


@pytest.fixture
def create_test_user():
    yield from create_resource(TestUserAPIControllerFixture)
