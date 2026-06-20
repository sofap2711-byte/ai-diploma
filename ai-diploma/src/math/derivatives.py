"""
Модуль с производными функций.

Здесь мы вычисляем производную выручки и ошибки.
Производная показывает, как быстро меняется выручка при изменении цены.
"""

from src.functions import revenue, loss_function

def revenue_derivative(price):
    """
    Производная функции выручки.
    
    Формула: Выручка = 100*price - 2*price²
    Производная: 100 - 4*price
    
    Аргументы:
        price (float): цена за единицу товара
    
    Возвращает:
        float: производная выручки по цене
    
    Пример:
        >>> revenue_derivative(10)  # 100 - 4*10 = 60
    """
    return 100 - 4 * price


def loss_derivative(price):
    """
    Производная функции ошибки.
    
    Так как loss = -revenue, то loss' = -revenue'
    Т.е. loss'(price) = -(100 - 4*price) = 4*price - 100
    
    Аргументы:
        price (float): цена за единицу товара
    
    Возвращает:
        float: производная ошибки по цене
    
    Пример:
        >>> loss_derivative(10)  # 4*10 - 100 = -60
    """
    return -revenue_derivative(price)
