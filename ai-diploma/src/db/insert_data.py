def clear_products(connection):
    # Создаём курсор — он нужен для любой SQL-команды
    cursor = connection.cursor()

    # DELETE FROM products  удаляем ВСЕ строки из таблицы products
    cursor.execute("DELETE FROM products")

    # Сохраняем изменения в файле БД
    connection.commit()

def clear_suppliers(connection):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM suppliers")     # очищаем таблицу поставщиков
    connection.commit()

def add_product(connection, name, supplier, category, boxes, price_per_box):
    cursor = connection.cursor()   #Функция добавляет новый товар в таблицу products

    # Считаем выручку в Python: коробки × цена за коробку
    revenue = boxes * price_per_box

    # INSERT INTO — добавляет новую строку в таблицу
    # VALUES (?, ?, ...) — вместо ? подставляются переданные значения
    # Это защищает от SQL-инъекций и автоматически конвертирует типы
    cursor.execute("""
        INSERT INTO products (name, supplier, category, boxes, price_per_box, revenue)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, supplier, category, boxes, price_per_box, revenue))

    # Обязательно сохраняем изменения
    connection.commit()

def add_supplier(connection, name, city, contact, rating, total_orders):
    cursor = connection.cursor()   #Функция добавляет нового поставщика в таблицу suppliers
    cursor.execute("""
        INSERT INTO suppliers (name, city, contact, rating, total_orders)
        VALUES (?, ?, ?, ?, ?)
    """, (name, city, contact, rating, total_orders))
    connection.commit()

def seed_demo_data(connection):
    """Заполняет базу демонстрационными данными"""

    # Сначала чистим таблицы, чтобы при повторном запуске не было дублей
    clear_products(connection)
    clear_suppliers(connection)

    # Список поставщиков — каждый элемент это кортеж (name, city, contact, rating, total_orders)
    suppliers_data = [
        ("ООО ТехноПост", "Москва", "technopost@mail.ru", 4.8, 120),
        ("ИП Иванов", "Казань", "ivanov@mail.ru", 4.5, 85),
        ("ООО ЭкранПлюс", "Санкт-Петербург", "ekranplus@mail.ru", 4.2, 60),
    ]
    for s in suppliers_data:
        # s[0], s[1]... — достаём элементы кортежа по порядку и передаём в функцию
        add_supplier(connection, s[0], s[1], s[2], s[3], s[4])

    # Список товаров — каждый элемент это (name, supplier, category, boxes, price_per_box)
    products_data = [
        ("Ноутбуки", "ООО ТехноПост", "Техника", 15, 70000.0),
        ("Мыши", "ООО ТехноПост", "Техника", 45, 1500.0),
        ("Клавиатуры", "ИП Иванов", "Техника", 30, 3500.0),
        ("Мониторы", "ООО ЭкранПлюс", "Техника", 12, 25000.0),
        ("Наушники", "ИП Иванов", "Аксессуары", 28, 5000.0),
    ]
    for p in products_data:
        add_product(connection, p[0], p[1], p[2], p[3], p[4])
