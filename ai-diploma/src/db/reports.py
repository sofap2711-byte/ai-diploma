def get_total_revenue(connection):
    cursor = connection.cursor()

    # SUM(revenue) — SQL складывает все значения в колонке revenue
    cursor.execute("SELECT SUM(revenue) FROM products")

    # fetchone() возвращает одну строку результата (кортеж), [0] — первое (и единственное) значение
    result = cursor.fetchone()[0]

    # Если таблица пустая, SUM вернёт None — заменяем на 0, чтобы не было ошибок
    return result if result is not None else 0

def get_average_price(connection):
    cursor = connection.cursor()

    # AVG(price_per_box) — считает среднее значение цены за коробку
    cursor.execute("SELECT AVG(price_per_box) FROM products")
    result = cursor.fetchone()[0]
    return result if result is not None else 0

def get_category_report(connection):
    cursor = connection.cursor()

    # GROUP BY category — объединяет строки с одинаковой категорией в одну группу
    # COUNT(*) — считает количество товаров в группе
    # SUM(revenue) — суммарная выручка группы
    # AVG(price_per_box) — средняя цена в группе
    cursor.execute("""
        SELECT category, COUNT(*), SUM(revenue), AVG(price_per_box)
        FROM products
        GROUP BY category
        ORDER BY SUM(revenue) DESC
    """)
    return cursor.fetchall()

def get_supplier_report(connection):
    cursor = connection.cursor()

    # GROUP BY supplier — группируем товары по поставщикам
    # COUNT(*) — сколько товаров у поставщика, SUM(revenue) — общая выручка
    cursor.execute("""
        SELECT supplier, COUNT(*), SUM(revenue)
        FROM products
        GROUP BY supplier
        ORDER BY SUM(revenue) DESC
    """)
    return cursor.fetchall()
