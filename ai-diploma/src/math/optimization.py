"""
Модуль с алгоритмом оптимизации (градиентный спуск).

Мы будем искать оптимальную цену, при которой выручка максимальна.
"""

from src.functions import revenue, loss_function
from src.derivatives import loss_derivative


def gradient_descent(start_price, learning_rate, steps):
    """
    Градиентный спуск для поиска оптимальной цены.
    
    Мы начинаем с произвольной цены и постепенно двигаемся к максимуму выручки.
    
    Аргументы:
        start_price (float): начальная цена
        learning_rate (float): скорость обучения (размер шага)
        steps (int): количество шагов
    
    Возвращает:
        list: история шагов (каждый шаг — словарь с ценой, выручкой и производной)
    
    Пример:
        >>> history = gradient_descent(start_price=5, learning_rate=0.1, steps=20)
    """
    price_current = start_price
    history = []
    
    for step in range(steps):
        # Текущая выручка и ошибка
        current_revenue = revenue(price_current)
        current_loss = loss_function(price_current)
        
        # Производная ошибки (показывает направление)
        derivative = loss_derivative(price_current)
        
        # Сохраняем в историю
        history.append({
            "step": step,
            "price": price_current,
            "revenue": current_revenue,
            "loss": current_loss,
            "derivative": derivative
        })
        
        # Обновляем цену: двигаемся против производной
        # Формула: price_new = price_old - learning_rate * derivative
        price_current = price_current - learning_rate * derivative
    
    return history


def find_optimal_price(history):
    """
    Находит оптимальную цену из истории градиентного спуска.
    
    Аргументы:
        history (list): история шагов
    
    Возвращает:
        dict: информация об оптимальной цене
    """
    # Берём последний шаг (самая близкая к оптимуму цена)
    last_step = history[-1]
    
    return {
        "optimal_price": last_step["price"],
        "max_revenue": last_step["revenue"],
        "steps": len(history)
    }
