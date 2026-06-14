def get_all_products(connection):     # получаем все товары из таблицы products
    cursor = connection.cursor()                    # берём курсор из подключения

    # SELECT * FROM products — выбрать все колонки и все строки из таблицы products
    cursor.execute("SELECT * FROM products")

    # fetchall() забирает все найденные строки и возвращает их как список кортежей
    return cursor.fetchall()

def get_all_suppliers(connection):  #Функция получает всех поставщиков из таблицы suppliers
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM suppliers")
    return cursor.fetchall()

def find_products_by_category(connection, category):       #Функция ищет все товары в указанной категории
    cursor = connection.cursor()

    # WHERE category = ? — фильтруем только строки с нужной категорией
    # Значение category подставляется безопасно через второй аргумент execute
    cursor.execute("SELECT * FROM products WHERE category = ?", (category,))
    return cursor.fetchall()

def find_products_by_supplier(connection, supplier):   #Функция ищет все товары от указанного поставщика
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products WHERE supplier = ?", (supplier,))
    return cursor.fetchall()

def get_top_products(connection, limit=3):   #Функция получает топ N товаров по выручке (revenue)
    cursor = connection.cursor()

    # ORDER BY revenue DESC — сортируем по убыванию выручки
    # LIMIT ? — ограничиваем результат первыми N записями
    cursor.execute("""
        SELECT name, supplier, revenue FROM products 
        ORDER BY revenue DESC LIMIT ?
    """, (limit,))
    return cursor.fetchall()
