"""
Модуль для визуализации данных.

Строим графики:
1. Функция выручки (парабола)
2. Шаги градиентного спуска
3. Оптимальная цена
"""

import numpy as np
import matplotlib.pyplot as plt

from src.functions import revenue, loss_function


def show_revenue_graph():
    """
    Строит график функции выручки от цены.
    """
    # Цены от 0 до 50 (больше 50 — отрицательное количество)
    prices = np.linspace(0, 50, 300)
    revenues = [revenue(p) for p in prices]
    
    plt.figure(figsize=(8, 5))
    plt.plot(prices, revenues, color='blue', linewidth=2, label='Выручка = price × (100 - 2·price)')
    
    # Находим максимум (вершина параболы)
    max_revenue = max(revenues)
    max_index = np.argmax(revenues)
    optimal_price = prices[max_index]
    
    plt.scatter([optimal_price], [max_revenue], color='red', s=100, zorder=5,
                label=f'Максимум: цена={optimal_price:.1f}, выручка={max_revenue:.0f}')
    
    plt.title("📈 Зависимость выручки от цены (складская задача)")
    plt.xlabel("Цена за единицу (руб.)")
    plt.ylabel("Выручка (руб.)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()
    
    return optimal_price, max_revenue


def show_optimization_progress(history):
    """
    Строит график движения к оптимальной цене.
    
    Аргументы:
        history (list): история шагов градиентного спуска
    """
    # Извлекаем данные из истории
    steps = [h["step"] for h in history]
    prices = [h["price"] for h in history]
    revenues = [h["revenue"] for h in history]
    
    # Строим график выручки
    plt.figure(figsize=(10, 6))
    
    # График функции выручки (фон)
    price_range = np.linspace(0, 50, 300)
    revenue_range = [revenue(p) for p in price_range]
    plt.plot(price_range, revenue_range, color='blue', linewidth=2, alpha=0.3, label='Функция выручки')
    
    # Шаги градиентного спуска
    plt.scatter(prices, revenues, color='red', s=60, zorder=5, label='Шаги оптимизации')
    plt.plot(prices, revenues, color='red', linestyle='--', linewidth=1, alpha=0.5)
    
    # Начальная и конечная точки
    plt.scatter([prices[0]], [revenues[0]], color='orange', s=100, zorder=6, label='Старт')
    plt.scatter([prices[-1]], [revenues[-1]], color='green', s=100, zorder=6, label='Финиш')
    
    plt.title("🚀 Градиентный спуск: поиск оптимальной цены")
    plt.xlabel("Цена за единицу (руб.)")
    plt.ylabel("Выручка (руб.)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()


def show_loss_graph():
    """
    Строит график функции ошибки (loss = -revenue).
    """
    prices = np.linspace(0, 50, 300)
    losses = [loss_function(p) for p in prices]
    
    plt.figure(figsize=(8, 5))
    plt.plot(prices, losses, color='red', linewidth=2, label='Ошибка: loss = -выручка')
    
    # Минимум ошибки = максимум выручки
    min_loss = min(losses)
    min_index = np.argmin(losses)
    optimal_price = prices[min_index]
    
    plt.scatter([optimal_price], [min_loss], color='green', s=100, zorder=5,
                label=f'Минимум ошибки: цена={optimal_price:.1f}, loss={min_loss:.0f}')
    
    plt.title("📉 Функция ошибки для градиентного спуска")
    plt.xlabel("Цена за единицу (руб.)")
    plt.ylabel("Ошибка (чем меньше, тем лучше)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()
    
    return optimal_price, min_loss


def print_history_table(history):
    """
    Выводит историю шагов в виде таблицы.
    
    Аргументы:
        history (list): история шагов
    """
    print("\n📊 ИСТОРИЯ ГРАДИЕНТНОГО СПУСКА")
    print("=" * 65)
    print(f"{'Шаг':>4} | {'Цена':>8} | {'Выручка':>10} | {'Производная':>12}")
    print("-" * 65)
    
    for step in history:
        print(f"{step['step']:>4} | {step['price']:>8.2f} | {step['revenue']:>10.2f} | {step['derivative']:>12.2f}")
    
    print("=" * 65)