from src.masks import get_mask_card_number
import pytest


@pytest.mark.parametrize('card_number, expected',[
                         ('1596837868705199', '1596 83** **** 5199'),
                         ('7158300734726758', '7158 30** **** 6758'),
                         ('6831982476737658', '6831 98** **** 7658'),
    ]
)


def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected

