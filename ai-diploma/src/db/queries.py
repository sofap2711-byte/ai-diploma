def get_all_products(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()

def get_all_suppliers(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM suppliers")
    return cursor.fetchall()

def find_products_by_category(connection, category):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products WHERE category = ?", (category,))
    return cursor.fetchall()

def find_products_by_supplier(connection, supplier):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products WHERE supplier = ?", (supplier,))
    return cursor.fetchall()

def get_top_products(connection, limit=3):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT name, supplier, revenue FROM products 
        ORDER BY revenue DESC LIMIT ?
    """, (limit,))
    return cursor.fetchall()