def create_products_table(connection):
    """Создаёт таблицу products для складского учёта"""
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        supplier TEXT,
        category TEXT,
        boxes INTEGER,
        price_per_box REAL,
        revenue REAL
    )
    """)
    connection.commit()

def create_suppliers_table(connection):
    """Создаёт таблицу suppliers"""
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS suppliers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        city TEXT,
        contact TEXT,
        rating REAL,
        total_orders INTEGER
    )
    """)
    connection.commit()

def create_all_tables(connection):
    """Создаёт все таблицы проекта"""
    create_products_table(connection)
    create_suppliers_table(connection)