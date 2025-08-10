import re
from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(acc_card_number: str) -> str:
    """Принимает название карты или счета и его номер и возвращает то же самое,
    но с маскированным номером"""

    acc_card_number_no_spaces = re.sub(" ", "", acc_card_number)
    just_numbers = re.sub(r"[^0-9]", "", acc_card_number_no_spaces)
    just_words = re.sub(r"[0-9]", "", acc_card_number_no_spaces)

    if len(just_numbers) == 16:
        masked_number = get_mask_card_number(just_numbers)
    elif len(just_numbers) == 20:
        masked_number = get_mask_account(just_numbers)
    else:
        raise ValueError("Это не номер карты или счета.")
    if 'visa' in just_words.lower():
        just_words_visa_space = just_words[:4] + ' ' + just_words[4:]
        masked_all = just_words_visa_space.title() + ' ' + masked_number
    elif 'mastercard' in just_words.lower():
        just_words_mastercard = 'MasterCard'
        masked_all = just_words_mastercard + ' ' + masked_number
    else:
        masked_all = just_words + ' ' + masked_number
    return masked_all


date_ = '2025-08-10T15:433dsafsdaf5:30'


# Не понимаю, почему программа выдает ошибку, хотя в других фунциях выдает текст ошибки. Помогите
def get_date(date_: str) -> str:
    """Приводит строку с датой к формату 'ДД.ММ.ГГГГ'"""
    try:
        dt = datetime.fromisoformat(date_)
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError(f"Не удалось распознать дату: {date_}")

print(get_date(date_))





