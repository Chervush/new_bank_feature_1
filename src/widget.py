import re


def mask_account_card(acc_card_number: str) -> str:
    just_numbers = re.sub(r"[^0-9]", '', acc_card_number)
    just_words = re.sub(r"[0-9 ]", '', acc_card_number)
    if len(just_numbers) == 16:
        masked_number = just_numbers[:4] + " " + just_numbers[4:6] + "** **** " + just_numbers[-4:]
    if len(just_numbers) == 20:
        masked_number = "**" + just_numbers[-4:]


    masked_all = just_words + ' ' + masked_number
    return masked_all


#card_acc = 'Maestro 1596837868705199'
#print(mask_account_card(card_acc))




