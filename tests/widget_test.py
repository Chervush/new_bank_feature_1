import pytest

from src.widget import mask_account_card, get_date

#Проверка функции mask_account_card с использованием номеров счетов и карт, с пробелами и без, со строчным написанием visa, mastercard
@pytest.mark.parametrize('acc_card_number, expected', [
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('Счет 64686473678894779589','Счет **9589'),
    ('MasterCard 7158300734726758','MasterCard 7158 30** **** 6758'),
    ('Счет 35383033474447895560','Счет **5560'),
    ('visa classic 6831982476737658','Visa Classic 6831 98** **** 7658'),
    ('Visa Platinum 8990922113665229','Visa Platinum 8990 92** **** 5229'),
    ('Visa Gold 5999414228426353','Visa Gold 5999 41** **** 6353'),
    ('Счет 73654108430135874305','Счет **4305'),
    ('Счет 736541084301358 7 4 3 0 5','Счет **4305'),
    ('Visa Gold 5999 4142 2842 6353','Visa Gold 5999 41** **** 6353')
]
                         )
def test_mask_account_card(acc_card_number, expected):
    assert mask_account_card(acc_card_number) == expected

#Проверка функции mask_account_card с использованием неправильных данных



@pytest.fixture
def date():
    return "2024-03-11T02:26:18.671407"
def test_get_date(date):
    assert get_date(date) == '11.03.2024'

