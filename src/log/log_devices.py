import logging
import ecs_logging
import time
from random import randint

# Инициализация логгера
logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('log/log_devices.json')
handler.setFormatter(ecs_logging.StdlibFormatter())
logger.addHandler(handler)

def log_message(method, message):
    """
    Функция для вызова метода логгера.

    Args:
        method: Метод логгера (info, warning, error, critical).
        message: Сообщение для записи в лог.
    """

    # Получение атрибута метода логгера по имени
    log_method = getattr(logger, method)

    # Вызов метода логгера
    log_method(message, extra={"http.request.body.content": message})
