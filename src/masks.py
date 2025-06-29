from typing import Union

def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция маскировки номера банковской карты"""

    masked_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return masked_number


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция маскировки номера банковского счета"""

    masked_number = "**" + account_number[-4:]
    return masked_number
