import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from functions import revenue, loss_function, get_product_info, PRODUCT_NAME, CURRENT_PRICE, CURRENT_REVENUE
from derivatives import loss_derivative
from optimization import gradient_descent, find_optimal_price
from visualization import show_all_graphs, print_history_table
from report_utils import save_report


def main():
    # Информация о товаре
    product_info = get_product_info()
    
    print("\n" + "=" * 60)
    print(f"   📦 СКЛАДСКОЙ УЧЁТ: ОПТИМИЗАЦИЯ ЦЕНЫ")
    print("=" * 60)
    
    print(f"\n📌 ТОВАР: {product_info['product_name']}")
    print(f"   Текущая цена: {product_info['current_price']:,} руб. за ящик")
    print(f"   Текущее количество: {product_info['current_boxes']} ящиков")
    print(f"   Текущая выручка: {product_info['current_revenue']:,} руб.")
    
    # Параметры градиентного спуска
    start_price = 50000      # начальная цена (ниже текущей)
    learning_rate = 0.00005  # скорость обучения
    steps = 30               # количество шагов
    
    print(f"\n🚀 ЗАПУСК ГРАДИЕНТНОГО СПУСКА")
    print("-" * 40)
    print(f"   Начальная цена: {start_price:,} руб.")
    print(f"   Скорость обучения: {learning_rate}")
    print(f"   Количество шагов: {steps}")
    
    # Запускаем градиентный спуск
    history = gradient_descent(start_price, learning_rate, steps)
    
    # Результат
    result = find_optimal_price(history)
    optimal_price = result['optimal_price']
    max_revenue = result['max_revenue']
    
    print("\n✅ ГРАДИЕНТНЫЙ СПУСК ЗАВЕРШЁН")
    print("-" * 40)
    print(f"   Оптимальная цена: {optimal_price:,.0f} руб.")
    print(f"   Максимальная выручка: {max_revenue:,.0f} руб.")
    
    # Сравнение с текущей ценой
    improvement = ((max_revenue - CURRENT_REVENUE) / CURRENT_REVENUE * 100)
    
    print("\n📊 СРАВНЕНИЕ:")
    print("-" * 40)
    print(f"   Текущая выручка: {CURRENT_REVENUE:,.0f} руб.")
    print(f"   Макс. выручка:   {max_revenue:,.0f} руб.")
    print(f"   Рост: +{improvement:.1f}%")
    print(f"   Рекомендуемая цена: {optimal_price:,.0f} руб.")
    print(f"   Текущая цена: {CURRENT_PRICE:,.0f} руб.")
    print(f"   Изменение цены: {((optimal_price - CURRENT_PRICE) / CURRENT_PRICE * 100):+.1f}%")
    
    # Показываем таблицу
    print_history_table(history)
    
    # Сохраняем отчёт
    save_report(history)
    
    # Показываем графики
    print("\n   🎨 ПОКАЗЫВАЕМ ВСЕ ГРАФИКИ...")
    print("=" * 60)
    print("   (Закрывайте каждое окно с графиком, чтобы увидеть следующий)")
    print("=" * 60)
    
    show_all_graphs(history)


if __name__ == "__main__":
    main()