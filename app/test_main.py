import datetime
from unittest import mock
import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "today_changed_date,expected_result",
    [
        pytest.param(
            datetime.date(2022, 2, 11),
            ["salmon", "chicken", "duck"],
            id="return all products if all outdated"
        ),
        pytest.param(
            datetime.date(2022, 2, 8),
            ["chicken", "duck"],
            id="return only chicken and duck if salmon not outdated"
        ),
        pytest.param(
            datetime.date(2022, 2, 3),
            ["duck"],
            id="return only duck if salmon and chicken not outdated"
        ),
        pytest.param(
            datetime.date(2022, 1, 31),
            [],
            id="return empty list if none outdated"
        ),
        pytest.param(
            datetime.date(2022, 2, 1),
            [],
            id="Product with expiration date equals today is not outdated."
        ),
    ]
)
def test_outdated_products(
        today_changed_date: callable,
        expected_result: str
) -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]
    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = today_changed_date
        assert outdated_products(products) == expected_result
