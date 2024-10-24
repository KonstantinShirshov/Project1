def get_mask_card_number(user_card_number: str) -> str:
    """Функция принимает строку и возвращает номер карты пользователя"""
    return f"{user_card_number[:4]} {user_card_number[4:6]}** **** {user_card_number[12:]}"


def get_mask_account(user_card_number: str) -> str:
    """Функция строку и возвращает маску счёта"""
    return f"**{user_card_number[-4:]}"
