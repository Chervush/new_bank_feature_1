import re

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
        return "Это не номер карты или счета."
    if 'visa' in just_words.lower():
        just_words_visa_space = just_words[:4] + ' ' + just_words[4:]
        masked_all = just_words_visa_space.title() + ' ' + masked_number
    elif 'mastercard' in just_words.lower():
        just_words_mastercard = 'MasterCard'
        masked_all = just_words_mastercard + ' ' + masked_number
    else:
        masked_all = just_words + ' ' + masked_number
    return masked_all


def get_date(date: str) -> str:
    """приводит строку с датой к формату 'ДД.ММ.ГГГГ'"""
    formatted_date = date[8:10] + "." + date[5:7] + "." + date[:4]
    return formatted_date
