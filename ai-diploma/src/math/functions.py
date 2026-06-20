"""
Модуль с функциями для расчёта выручки склада.
Используем РЕАЛЬНЫЕ данные из твоей базы данных.
"""

# ============================================================
# РЕАЛЬНЫЕ ДАННЫЕ ИЗ ТВОЕЙ БАЗЫ
# ============================================================

PRODUCT_NAME = "Ноутбуки"
CURRENT_PRICE = 70000      # текущая цена за ящик (из базы)
CURRENT_BOXES = 15         # текущее количество ящиков (из базы)
CURRENT_REVENUE = CURRENT_PRICE * CURRENT_BOXES  # 1 050 000 руб.


def quantity(price):
    """
    Количество проданных ящиков в зависимости от цены.
    
    Модель: чем выше цена, тем меньше покупают.
    Формула: Q = 100 - 0.001 * price
    
    Аргументы:
        price (float): цена за ящик
    
    Возвращает:
        float: количество ящиков
    
    Пример:
        >>> quantity(70000)  # 100 - 0.001*70000 = 30
    """
    return 100 - 0.001 * price


def revenue(price):
    """
    Выручка = Цена × Количество
    
    Аргументы:
        price (float): цена за ящик
    
    Возвращает:
        float: выручка
    """
    return price * quantity(price)


def loss_function(price):
    """
    Функция ошибки (для градиентного спуска).
    Берём ОТРИЦАТЕЛЬНУЮ выручку, чтобы искать минимум.
    """
    return -revenue(price)


def get_product_info():
    """
    Возвращает информацию о текущем товаре.
    """
    return {
        "product_name": PRODUCT_NAME,
        "current_price": CURRENT_PRICE,
        "current_boxes": CURRENT_BOXES,
        "current_revenue": CURRENT_REVENUE
    }
