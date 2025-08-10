import re
from typing import Union


def get_mask_card_number(card_number: Union[str]) -> str:
    """Функция маскировки номера банковской карты"""

    card_number_no_spaces = re.sub(" ", "", card_number)

    if len(card_number_no_spaces) < 16 or not card_number_no_spaces.isalnum():
        raise ValueError("Это не номер карты")

    masked_number: str = (
        card_number_no_spaces[:4] + " " + card_number_no_spaces[4:6] + "** **** " + card_number_no_spaces[-4:]
    )

    return masked_number


def get_mask_account(account_number: Union[str]) -> str:
    """Функция маскировки номера банковского счета"""

    account_number_no_spaces = re.sub(" ", "", account_number)

    if len(account_number_no_spaces) < 20 or not account_number_no_spaces.isalnum():
        raise ValueError("Это не номер счета")

    masked_number = "**" + account_number_no_spaces[-4:]

    return masked_number

