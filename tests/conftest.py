import pytest
from scr.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def numbers():
    return "0000 0000 0001 1111"


@pytest.mark.parametrize("descriptions", ["Перевод с карты на карту"])
def test_transaction_descriptions(transactions, descriptions):
    transaction = transaction_descriptions(transactions)
    assert next(transaction) == descriptions
