from scr.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency() -> None:
    assert list(
        filter_by_currency(
            [
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {
                        "amount": "79114.93",
                        "currency": {"name": "USD", "code": "USD"},
                    },
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {
                        "amount": "43318.34",
                        "currency": {"name": "руб.", "code": "RUB"},
                    },
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
            ],
            "USD",
        )
    ) == [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        }
    ]


def test_filter_by_currency_noUSD() -> None:
    assert (
        list(
            filter_by_currency(
                [
                    {
                        "id": 939719570,
                        "state": "EXECUTED",
                        "date": "2018-06-30T02:08:58.425572",
                        "operationAmount": {
                            "amount": "9824.07",
                            "currency": {"name": "RUB", "code": "RUB"},
                        },
                        "description": "Перевод организации",
                        "from": "Счет 75106830613657916952",
                        "to": "Счет 11776614605963066702",
                    }
                ],
                "USD",
            )
        )
        == []
    )


def test_filter_by_currency_empty() -> None:
    assert list(filter_by_currency([], "USD")) == []


def test_transaction_descriptions() -> None:
    descriptions = transaction_descriptions(
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {"name": "USD", "code": "USD"},
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                    "amount": "79114.93",
                    "currency": {"name": "USD", "code": "USD"},
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
            },
        ]
    )
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"


def test_card_number_generator() -> None:
    number = card_number_generator(11111, 11113)
    assert next(number) == "0000 0000 0001 1111"
    assert next(number) == "0000 0000 0001 1112"
    assert next(number) == "0000 0000 0001 1113"


def test_card_number_generator(numbers):
    assert next(card_number_generator(11111, 11111)) == numbers
