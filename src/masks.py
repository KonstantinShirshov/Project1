import logging

logger = logging.getLogger("masks.py")
file_handler = logging.FileHandler("../logs/masks.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(user_card_number: str) -> str:
    """Функция принимает строку и возвращает номер карты пользователя"""
    logger.info("Маскируем номер карты клиента")
    return f"{user_card_number[:4]} {user_card_number[4:6]}** **** {user_card_number[12:]}"


def get_mask_account(user_card_number: str) -> str:
    """Функция строку и возвращает маску счёта"""
    logger.info("Маскируем номер счёта клиента")
    return f"**{user_card_number[-4:]}"


# if __name__ == "__main__":
#     print(get_mask_card_number("7000792289606361"))
#     print(get_mask_account("35383033474447895560"))
