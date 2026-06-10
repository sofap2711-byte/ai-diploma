def get_all_products(connection):
    cursor = connection.cursor()                    # берём курсор из подключения

    # SELECT * FROM products — выбрать все колонки и все строки из таблицы products
    cursor.execute("SELECT * FROM products")

    # fetchall() забирает все найденные строки и возвращает их как список кортежей
    return cursor.fetchall()

def get_all_suppliers(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM suppliers")
    return cursor.fetchall()

def find_products_by_category(connection, category):
    cursor = connection.cursor()

    # WHERE category = ? — фильтруем только строки с нужной категорией
    # Значение category подставляется безопасно через второй аргумент execute
    cursor.execute("SELECT * FROM products WHERE category = ?", (category,))
    return cursor.fetchall()

def find_products_by_supplier(connection, supplier):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products WHERE supplier = ?", (supplier,))
    return cursor.fetchall()

def get_top_products(connection, limit=3):
    cursor = connection.cursor()

    # ORDER BY revenue DESC — сортируем по убыванию выручки
    # LIMIT ? — ограничиваем результат первыми N записями
    cursor.execute("""
        SELECT name, supplier, revenue FROM products 
        ORDER BY revenue DESC LIMIT ?
    """, (limit,))
    return cursor.fetchall()
