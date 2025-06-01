import logging
import pathlib
import textwrap
from typing import Union

base_path = pathlib.Path(__file__).resolve().parent.parent
directory = base_path / "logs/masks.log"

# logging.basicConfig(
#     filename=directory,
#     filemode="w",
#     format="%(asctime)s %(filename)s %(levelname)s: %(message)s",
#     level="INFO",
#     encoding="utf-8",
# )

logger = logging.getLogger("masks")
logger_handler = logging.FileHandler(directory, encoding="utf-8", mode="w")
logger_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
logger_handler.setFormatter(logger_formatter)
logger.addHandler(logger_handler)
logger.setLevel("DEBUG")


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция маскировки номера банковской карты"""
    logger.debug("Запуск функции get_mask_card_number")

    if isinstance(card_number, int):
        logger.info("Перевод типа данных с номером карты в строковый формат")
        card_number = str(card_number)

    if len(card_number) == 16 and card_number.isdigit():
        logger.info("Маскировка номера карты")
        return " ".join(textwrap.wrap(f"{card_number[:6]}******{card_number[-4:]}", 4))
    else:
        logger.error("Номер карты не соответствует заданному формату: 16 цифровых символов")
        raise ValueError("Номер банковской карты должен состоять из 16-ти цифровых символов")


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функцию маскировки номера банковского счета"""
    logger.debug("Запуск функции get_mask_account")

    if isinstance(account_number, int):
        logger.info("Перевод типа данных с номером банковского счета в строковый формат")
        account_number = str(account_number)
    if len(account_number) == 20 and account_number.isdigit():
        logger.info("Маскировка номера банковского счета")
        return f"**{str(account_number)[-4:]}"
    else:
        logger.error("Номер банковского счета не соответствует заданному формату: 20 цифровых символов")
        raise ValueError("Номер банковского счета должен состоять из 20-ти цифровых символов")
