def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""

    card_number_str = str(card_number)
    if len(card_number_str) != 16:
        return "Это не номер карты!"

    else:
        masked_number = card_number_str[:4] + " " + card_number_str[4:6] + "** **** " + card_number_str[-4:]
        return masked_number


def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера банковского счета"""
    account_number_str = str(account_number)
    if len(account_number_str) != 20:
        return "Это не номер cчета!"

    else:
        masked_number = "**" + account_number_str[-4:]
        return masked_number
