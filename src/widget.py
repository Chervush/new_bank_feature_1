import re
from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(acc_card_number: str) -> str:
    """Принимает название карты или счета и его номер и возвращает то же самое,
    но с маскированным номером"""

    just_numbers = re.sub(r"[^0-9]", '', acc_card_number)
    just_words = re.sub(r"[0-9 ]", '', acc_card_number)
    if len(just_numbers) == 16:
        masked_number = get_mask_card_number(just_numbers)
    elif len(just_numbers) == 20:
        masked_number = get_mask_account(just_numbers)
    else:
        return 'Это не номер карты или счета.'


    masked_all = just_words + ' ' + masked_number
    return masked_all


def get_date(date: str) -> str:
    """приводит строку с датой к формату 'ДД.ММ.ГГГГ'"""
    formatted_date = date[8:10] + '.' + date[5:7] + '.' + date[:4]
    return formatted_date


#date = "2024-03-11T02:26:18.671407"
#print(get_date(date))
#card_acc = 'Maestro 1596837868705199'
#print(mask_account_card(card_acc))




