def get_total_revenue(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT SUM(revenue) FROM products")
    result = cursor.fetchone()[0]
    return result if result is not None else 0

def get_average_price(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT AVG(price_per_box) FROM products")
    result = cursor.fetchone()[0]
    return result if result is not None else 0

def get_category_report(connection):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT category, COUNT(*), SUM(revenue), AVG(price_per_box)
        FROM products
        GROUP BY category
        ORDER BY SUM(revenue) DESC
    """)
    return cursor.fetchall()

def get_supplier_report(connection):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT supplier, COUNT(*), SUM(revenue)
        FROM products
        GROUP BY supplier
        ORDER BY SUM(revenue) DESC
    """)
    return cursor.fetchall()