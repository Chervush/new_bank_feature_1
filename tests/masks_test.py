from src.masks import get_mask_card_number, get_mask_account
import pytest


#общий тест для функции get_mask_card_number включая написание номера карты с пробелами
@pytest.mark.parametrize('card_number, expected',[
                         ('1596837868705199', '1596 83** **** 5199'),
                         ('7158300734726758', '7158 30** **** 6758'),
                         ('6831982476737658', '6831 98** **** 7658'),
                         ('6831 9824 7673 7658', '6831 98** **** 7658'),
    ]
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


#тест для функции get_mask_card_number с неправильными входными данными
def test_get_mask_card_number_wrong_number(wrong_number):
    with pytest.raises(ValueError):
        get_mask_card_number(wrong_number)


#общий тест для функции get_mask_account включая написание счета с пробелами
@pytest.mark.parametrize('account_number, expected',[
                         ('73654108430135874305', '**4305'),
                         ('64686473678894779589', '**9589'),
                         ('35383033474447895560', '**5560'),
                         ('3538 3033 4744 4789 5 5 6 0', '**5560'),
    ]
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected

#тест для функции get_mask_account с неправильными входными данными
def test_get_mask_account_wrong_number(wrong_number):
    with pytest.raises(ValueError):
        get_mask_account(wrong_number)
