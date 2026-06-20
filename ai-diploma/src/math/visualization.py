import numpy as np
import matplotlib.pyplot as plt
import os

from functions import revenue, loss_function, quantity, PRODUCT_NAME, CURRENT_PRICE, CURRENT_REVENUE

os.makedirs("data/graphs", exist_ok=True)


def show_all_graphs(history):
    """Показывает ВСЕ графики с подписями"""
    
    first = history[0]
    last = history[-1]
    
    optimal_price = last["price"]
    max_revenue = last["revenue"]
    improvement = ((max_revenue - CURRENT_REVENUE) / CURRENT_REVENUE * 100)
    
    # Диапазон цен: от 0 до 150 000 руб.
    prices = np.linspace(0, 150000, 300)
    revenues = [revenue(p) for p in prices]
    
    # ============================================================
    # ГРАФИК 1: Выручка от цены
    # ============================================================
    plt.figure(figsize=(10, 6))
    plt.plot(prices, revenues, color='blue', linewidth=2, label='Выручка')
    
    max_revenue_analytical = max(revenues)
    max_index = np.argmax(revenues)
    optimal_price_analytical = prices[max_index]
    
    plt.scatter([optimal_price_analytical], [max_revenue_analytical], color='red', s=100, zorder=5, 
                label=f'Оптимальная цена: {optimal_price_analytical/1000:.0f} тыс. руб.')
    plt.axvline(x=optimal_price_analytical, color='red', linestyle='--', alpha=0.5)
    
    # Текущая цена
    plt.scatter([CURRENT_PRICE], [CURRENT_REVENUE], color='orange', s=120, zorder=6,
                label=f'Текущая цена: {CURRENT_PRICE/1000:.0f} тыс. руб.')
    plt.axvline(x=CURRENT_PRICE, color='orange', linestyle='--', alpha=0.5)
    
    # Добавляем текстовую информацию на график
    info_text = f"""
    📌 Товар: {PRODUCT_NAME}
    📊 Текущая цена: {CURRENT_PRICE/1000:.0f} тыс. руб.
    🎯 Оптимальная цена: {optimal_price_analytical/1000:.0f} тыс. руб.
    📈 Рост выручки: +{improvement:.0f}%
    """
    plt.text(0.02, 0.95, info_text, transform=plt.gca().transAxes, 
             fontsize=10, verticalalignment='top', 
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.title(f"📈 График 1: Выручка от цены ({PRODUCT_NAME})")
    plt.xlabel("Цена за ящик (тыс. руб.)")
    plt.ylabel("Выручка (руб.)")
    plt.grid(True, alpha=0.3)
    plt.legend(loc='lower right')
    plt.savefig("data/graphs/01_revenue.png", dpi=150, bbox_inches='tight')
    plt.show()


    # ============================================================
    # ГРАФИК 2: Шаги градиентного спуска
    # ============================================================
    steps = [h["step"] for h in history]
    prices_hist = [h["price"] for h in history]
    revenues_hist = [h["revenue"] for h in history]
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(prices, revenues, color='blue', linewidth=2, alpha=0.3, label='Функция выручки')
    plt.scatter(prices_hist, revenues_hist, color='red', s=60, zorder=5, label='Шаги')
    plt.plot(prices_hist, revenues_hist, color='red', linestyle='--', linewidth=1, alpha=0.5)
    
    plt.scatter([prices_hist[0]], [revenues_hist[0]], color='orange', s=120, zorder=6,
                label=f'Старт: {prices_hist[0]/1000:.0f} тыс. руб.')
    plt.scatter([prices_hist[-1]], [revenues_hist[-1]], color='green', s=120, zorder=6,
                label=f'Финиш: {prices_hist[-1]/1000:.0f} тыс. руб.')
    
    info_text = f"""
    📌 Товар: {PRODUCT_NAME}
    🏁 Старт: {prices_hist[0]/1000:.0f} тыс. руб.
    🎯 Финиш: {prices_hist[-1]/1000:.0f} тыс. руб.
    📈 Шагов: {len(history)}
    """
    plt.text(0.02, 0.95, info_text, transform=plt.gca().transAxes, 
             fontsize=10, verticalalignment='top', 
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.title(f"📈 График 2: Градиентный спуск для {PRODUCT_NAME}")
    plt.xlabel("Цена за ящик (тыс. руб.)")
    plt.ylabel("Выручка (руб.)")
    plt.grid(True, alpha=0.3)
    plt.legend(loc='lower right')
    plt.savefig("data/graphs/02_optimization.png", dpi=150, bbox_inches='tight')
    plt.show()


    # ============================================================
    # ГРАФИК 3: Функция ошибки
    # ============================================================
    losses = [loss_function(p) for p in prices]
    
    plt.figure(figsize=(10, 6))
    plt.plot(prices, losses, color='red', linewidth=2, label='Ошибка')
    
    min_loss = min(losses)
    min_index = np.argmin(losses)
    optimal_price_loss = prices[min_index]
    
    plt.scatter([optimal_price_loss], [min_loss], color='green', s=100, zorder=5,
                label=f'Минимум: {optimal_price_loss/1000:.0f} тыс. руб.')
    plt.axvline(x=optimal_price_loss, color='green', linestyle='--', alpha=0.5)
    
    info_text = f"""
    📌 Товар: {PRODUCT_NAME}
    🎯 Минимум ошибки: {optimal_price_loss/1000:.0f} тыс. руб.
    📉 Чем ниже, тем лучше
    """
    plt.text(0.02, 0.95, info_text, transform=plt.gca().transAxes, 
             fontsize=10, verticalalignment='top', 
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.title(f"📈 График 3: Функция ошибки для {PRODUCT_NAME}")
    plt.xlabel("Цена за ящик (тыс. руб.)")
    plt.ylabel("Ошибка (чем меньше, тем лучше)")
    plt.grid(True, alpha=0.3)
    plt.legend(loc='lower right')
    plt.savefig("data/graphs/03_loss.png", dpi=150, bbox_inches='tight')
    plt.show()


    # ============================================================
    # ГРАФИК 4: Изменение цены
    # ============================================================
    plt.figure(figsize=(10, 6))
    plt.plot(steps, prices_hist, color='purple', linewidth=2, marker='o', markersize=6)
    plt.axhline(y=optimal_price, color='red', linestyle='--', alpha=0.7,
                label=f'Оптимальная цена: {optimal_price/1000:.0f} тыс. руб.')
    plt.axhline(y=CURRENT_PRICE, color='orange', linestyle='--', alpha=0.5,
                label=f'Текущая цена: {CURRENT_PRICE/1000:.0f} тыс. руб.')
    
    info_text = f"""
    📌 Товар: {PRODUCT_NAME}
    🏁 Старт: {prices_hist[0]/1000:.0f} тыс. руб.
    🎯 Финиш: {prices_hist[-1]/1000:.0f} тыс. руб.
    📈 Шагов: {len(history)}
    """
    plt.text(0.02, 0.95, info_text, transform=plt.gca().transAxes, 
             fontsize=10, verticalalignment='top', 
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.title(f"📈 График 4: Изменение цены {PRODUCT_NAME}")
    plt.xlabel("Шаг градиентного спуска")
    plt.ylabel("Цена (тыс. руб.)")
    plt.grid(True, alpha=0.3)
    plt.legend(loc='lower right')
    plt.savefig("data/graphs/04_price_change.png", dpi=150, bbox_inches='tight')
    plt.show()


    # ============================================================
    # ГРАФИК 5: Рост выручки
    # ============================================================
    plt.figure(figsize=(10, 6))
    plt.plot(steps, revenues_hist, color='green', linewidth=2, marker='s', markersize=6)
    plt.axhline(y=max_revenue, color='red', linestyle='--', alpha=0.7,
                label=f'Макс. выручка: {max_revenue/1000:.0f} тыс. руб.')
    plt.axhline(y=CURRENT_REVENUE, color='orange', linestyle='--', alpha=0.5,
                label=f'Текущая выручка: {CURRENT_REVENUE/1000:.0f} тыс. руб.')
    
    info_text = f"""
    📌 Товар: {PRODUCT_NAME}
    📊 Текущая выручка: {CURRENT_REVENUE/1000:.0f} тыс. руб.
    🎯 Макс. выручка: {max_revenue/1000:.0f} тыс. руб.
    📈 Рост: +{improvement:.0f}%
    """
    plt.text(0.02, 0.95, info_text, transform=plt.gca().transAxes, 
             fontsize=10, verticalalignment='top', 
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.title(f"📈 График 5: Рост выручки для {PRODUCT_NAME}")
    plt.xlabel("Шаг градиентного спуска")
    plt.ylabel("Выручка (тыс. руб.)")
    plt.grid(True, alpha=0.3)
    plt.legend(loc='lower right')
    plt.savefig("data/graphs/05_revenue_growth.png", dpi=150, bbox_inches='tight')
    plt.show()


    # ============================================================
    # ГРАФИК 6: Производная
    # ============================================================
    derivatives = [h["derivative"] for h in history]
    
    plt.figure(figsize=(10, 6))
    plt.plot(steps, derivatives, color='orange', linewidth=2, marker='d', markersize=6)
    plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
    
    info_text = f"""
    📌 Товар: {PRODUCT_NAME}
    📉 Производная → 0 = мы у цели
    🎯 Финальное значение: {derivatives[-1]:.2f}
    """
    plt.text(0.02, 0.95, info_text, transform=plt.gca().transAxes, 
             fontsize=10, verticalalignment='top', 
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.title(f"📈 График 6: Производная (скорость изменения) для {PRODUCT_NAME}")
    plt.xlabel("Шаг градиентного спуска")
    plt.ylabel("Производная (чем ближе к 0, тем лучше)")
    plt.grid(True, alpha=0.3)
    plt.savefig("data/graphs/06_derivative.png", dpi=150, bbox_inches='tight')
    plt.show()


    # ============================================================
    # ГРАФИК 7: Сравнение функций
    # ============================================================
    x = np.linspace(0.1, 10, 300)
    
    y_linear = x
    y_square = x ** 2
    y_log = np.log(x)
    y_exp = 2 ** x
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y_linear, label='Линейная: y = x', linewidth=2)
    plt.plot(x, y_square, label='Квадратичная: y = x²', linewidth=2)
    plt.plot(x, y_log, label='Логарифмическая: y = ln(x)', linewidth=2)
    plt.plot(x, y_exp, label='Показательная: y = 2ˣ', linewidth=2)
    
    info_text = """
    📚 Сравнение элементарных функций
    (из уроков 1-2)
    
    Линейная → равномерный рост
    Квадратичная → ускоренный рост
    Логарифмическая → замедленный рост
    Показательная → взрывной рост
    """
    plt.text(0.02, 0.95, info_text, transform=plt.gca().transAxes, 
             fontsize=10, verticalalignment='top', 
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.title("📈 График 7: Сравнение элементарных функций")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, alpha=0.3)
    plt.legend(loc='upper left')
    plt.savefig("data/graphs/07_functions_comparison.png", dpi=150, bbox_inches='tight')
    plt.show()


    # ============================================================
    # ГРАФИК 8: Влияние скорости обучения
    # ============================================================
    learning_rates = [0.00001, 0.00003, 0.00005, 0.0001, 0.0002]
    final_prices = []
    
    for lr in learning_rates:
        from optimization import gradient_descent
        test_history = gradient_descent(start_price=50000, learning_rate=lr, steps=30)
        final_prices.append(test_history[-1]["price"])
    
    plt.figure(figsize=(10, 6))
    plt.plot(learning_rates, final_prices, color='darkblue', linewidth=2, marker='o', markersize=8)
    plt.axhline(y=optimal_price, color='red', linestyle='--', alpha=0.7,
                label=f'Оптимальная цена: {optimal_price/1000:.0f} тыс. руб.')
    
    info_text = f"""
    📌 Товар: {PRODUCT_NAME}
    📊 Анализ чувствительности
    
    Чем выше скорость обучения,
    тем быстрее алгоритм находит решение,
    но может "перескочить" оптимум.
    """
    plt.text(0.02, 0.95, info_text, transform=plt.gca().transAxes, 
             fontsize=10, verticalalignment='top', 
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.title(f"📈 График 8: Влияние скорости обучения ({PRODUCT_NAME})")
    plt.xlabel("Скорость обучения (learning rate)")
    plt.ylabel("Финальная цена (тыс. руб.)")
    plt.grid(True, alpha=0.3)
    plt.legend(loc='lower right')
    plt.savefig("data/graphs/08_learning_rate_analysis.png", dpi=150, bbox_inches='tight')
    plt.show()


    # ============================================================
    # ГРАФИК 9: Сравнение ДО и ПОСЛЕ
    # ============================================================
    labels = ['Текущая\nцена', 'Оптимальная\nцена']
    values = [CURRENT_REVENUE, max_revenue]
    colors = ['orange', 'green']
    
    plt.figure(figsize=(8, 6))
    bars = plt.bar(labels, values, color=colors, width=0.5)
    
    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(values)*0.02,
                 f'{value/1000:.0f} тыс. руб.', ha='center', va='bottom', fontsize=12)
    
    info_text = f"""
    📌 Товар: {PRODUCT_NAME}
    📊 Рост выручки: +{improvement:.0f}%
    🎯 Рекомендуемая цена: {optimal_price/1000:.0f} тыс. руб.
    """
    plt.text(0.02, 0.95, info_text, transform=plt.gca().transAxes, 
             fontsize=10, verticalalignment='top', 
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.title(f"📈 График 9: Сравнение выручки ДО и ПОСЛЕ ({PRODUCT_NAME})")
    plt.ylabel("Выручка (тыс. руб.)")
    plt.grid(True, alpha=0.3, axis='y')
    plt.savefig("data/graphs/09_before_after.png", dpi=150, bbox_inches='tight')
    plt.show()


def print_history_table(history):
    """Выводит таблицу шагов градиентного спуска"""
    print("\n📊 ИСТОРИЯ ГРАДИЕНТНОГО СПУСКА")
    print("=" * 70)
    print(f"{'Шаг':>4} | {'Цена (тыс.)':>12} | {'Выручка (тыс.)':>16} | {'Производная':>12}")
    print("-" * 70)
    
    for step in history:
        price_k = step['price'] / 1000
        revenue_k = step['revenue'] / 1000
        print(f"{step['step']:>4} | {price_k:>12.1f} | {revenue_k:>16.1f} | {step['derivative']:>12.2f}")
    
    print("=" * 70)