from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: str) -> str:
    """Функция, которая обрабатывает информачию о картах и счетах"""
    original_number = card_info.split()[-1]
    if len(original_number) == 16:
        card_number = get_mask_card_number(original_number)
        result = f"{card_info[:-16]}{card_number}"
    elif len(original_number) == 20:
        account_number = get_mask_account(original_number)
        result = f"{card_info[:-20]}{account_number}"
    return result


def get_date(date_info: str) -> str:
    """Функция, которая принимает дату в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" """
    year, month, day = date_info.split("T")[0].split("-")
    return f"{day}.{month}.{year}"


print(get_date("2024-03-11T02:26:18.671407"))
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 35383033474447895560"))
