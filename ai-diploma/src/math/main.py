"""
Главный файл проекта.

Запускает весь проект:
1. Строит график выручки
2. Запускает градиентный спуск
3. Выводит результаты
4. Сохраняет отчёт
"""

from src.functions import revenue, loss_function
from src.derivatives import loss_derivative
from src.optimization import gradient_descent, find_optimal_price
from src.visualization import show_revenue_graph, show_optimization_progress, show_loss_graph, print_history_table
from src.report_utils import save_report


def main():
    """Главная функция проекта."""
    
    print("\n" + "=" * 60)
    print("   📦 СКЛАДСКОЙ УЧЁТ: ОПТИМИЗАЦИЯ ЦЕНЫ")
    print("=" * 60)
    
    # 1. Строим график выручки
    print("\n📈 1. График функции выручки")
    print("-" * 40)
    optimal_price_analytical, max_revenue_analytical = show_revenue_graph()
    
    # 2. Запускаем градиентный спуск
    print("\n🚀 2. Градиентный спуск")
    print("-" * 40)
    
    start_price = 5        # начальная цена (далеко от оптимума)
    learning_rate = 0.05   # скорость обучения (маленький шаг)
    steps = 30             # количество шагов
    
    print(f"   Начальная цена: {start_price} руб.")
    print(f"   Скорость обучения: {learning_rate}")
    print(f"   Количество шагов: {steps}")
    
    history = gradient_descent(start_price, learning_rate, steps)
    
    # 3. Показываем историю
    print_history_table(history)
    
    # 4. График движения к оптимуму
    print("\n📊 3. График движения к оптимальной цене")
    print("-" * 40)
    show_optimization_progress(history)
    
    # 5. График функции ошибки
    print("\n📉 4. График функции ошибки")
    print("-" * 40)
    show_loss_graph()
    
    # 6. Анализируем результат
    print("\n📊 5. Анализ результата")
    print("-" * 40)
    
    result = find_optimal_price(history)
    
    print(f"   🎯 Оптимальная цена: {result['optimal_price']:.2f} руб.")
    print(f"   💰 Максимальная выручка: {result['max_revenue']:.0f} руб.")
    print(f"   📈 Точное значение: {optimal_price_analytical:.2f} руб. (выручка {max_revenue_analytical:.0f} руб.)")
    
    # 7. Сохраняем отчёт
    print("\n📄 6. Сохранение отчёта")
    print("-" * 40)
    save_report(history)
    
    # 8. Итог
    print("\n" + "=" * 60)
    print("   ✅ ПРОЕКТ УСПЕШНО ЗАВЕРШЁН!")
    print("=" * 60)
    print("\n💡 Вывод:")
    print(f"   Градиентный спуск нашёл оптимальную цену: {result['optimal_price']:.1f} руб.")
    print(f"   При которой выручка составляет: {result['max_revenue']:.0f} руб.")
    print("   Это близко к точному математическому решению!")
    print("\n🎉 Проект готов к показу преподавателю!")


if __name__ == "__main__":
    main()