import sqlite3
from pathlib import Path

def get_connection():         #Функция создаёт подключение к базе данных warehouse_project.db
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    db_path = data_dir / "warehouse_project.db"
    return sqlite3.connect(db_path)

def create_tables(conn):        #Функция создаёт таблицы в базе данных, если они ещё не существуют
    cursor = conn.cursor()
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
    conn.commit()

def add_product(conn, name, supplier, category, boxes, price_per_box):      #Функция добавляет новый товар в таблицу products
    cursor = conn.cursor()
    revenue = boxes * price_per_box
    cursor.execute("""
        INSERT INTO products (name, supplier, category, boxes, price_per_box, revenue)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, supplier, category, boxes, price_per_box, revenue))
    conn.commit()

def add_supplier(conn, name, city, contact, rating, total_orders):      #Функция добавляет нового поставщика в таблицу suppliers
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO suppliers (name, city, contact, rating, total_orders)
        VALUES (?, ?, ?, ?, ?)
    """, (name, city, contact, rating, total_orders))
    conn.commit()

def clear_data(conn):        #Функция полностью очищает все таблицы в базе данных
    conn.execute("DELETE FROM products")
    conn.execute("DELETE FROM suppliers")

def load_demo_data(conn):        #Функция загружает демонстрационные данные в базу
    clear_data(conn)
    
    # Поставщики
    suppliers = [
        ("ООО ТехноПост", "Москва", "technopost@mail.ru", 4.8, 120),
        ("ИП Иванов", "Казань", "ivanov@mail.ru", 4.5, 85),
        ("ООО ЭкранПлюс", "Санкт-Петербург", "ekranplus@mail.ru", 4.2, 60),
    ]
    for s in suppliers:
        add_supplier(conn, s[0], s[1], s[2], s[3], s[4])
    
    # Товары
    products = [
        ("Ноутбуки", "ООО ТехноПост", "Техника", 15, 70000.0),
        ("Мыши", "ООО ТехноПост", "Техника", 45, 1500.0),
        ("Клавиатуры", "ИП Иванов", "Техника", 30, 3500.0),
        ("Мониторы", "ООО ЭкранПлюс", "Техника", 12, 25000.0),
        ("Наушники", "ИП Иванов", "Аксессуары", 28, 5000.0),
        ("Кабели", "ИП Иванов", "Аксессуары", 50, 500.0),
        ("Вебкамеры", "ООО ЭкранПлюс", "Техника", 18, 8000.0),
    ]
    for p in products:
        add_product(conn, p[0], p[1], p[2], p[3], p[4])

                      # ФУНКЦИИ ДЛЯ КРАСИВОГО ВЫВОДА ОТЧЁТОВ

def print_header(title):   # Функция выводит красивый заголовок с рамкой
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)

def print_section(title):      # Функция выводит раздел с декоративной линией
    print("\n" + "-" * 50)
    print(f" {title}")
    print("-" * 50)

def show_products_report(conn):     #Функция показывает подробный отчёт по всем товарам
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name, supplier, category, boxes, price_per_box, revenue 
        FROM products 
        ORDER BY revenue DESC
    """)
    products = cursor.fetchall()
    
    print_section("📦 ВСЕ ТОВАРЫ НА СКЛАДЕ")
    print(f"{'Название':<20} {'Поставщик':<20} {'Категория':<12} {'Ящиков':>8} {'Цена за ящ':>12} {'Выручка':>15}")
    print("-" * 90)
    
    total_revenue = 0
    for p in products:
        print(f"{p[0]:<20} {p[1]:<20} {p[2]:<12} {p[3]:>8} {p[4]:>11,.0f} руб. {p[5]:>13,.0f} руб.")
        total_revenue += p[5]
    
    print("-" * 90)
    print(f"{'ИТОГО:':<60} {total_revenue:>13,.0f} руб.")
    print(f"Всего товаров: {len(products)}")

def show_suppliers_report(conn):      #Функция показывает отчёт по всем поставщикам
    cursor = conn.cursor()
    cursor.execute("SELECT name, city, rating, total_orders FROM suppliers ORDER BY rating DESC")
    suppliers = cursor.fetchall()
    
    print_section("🏢 ПОСТАВЩИКИ")
    print(f"{'Название':<25} {'Город':<20} {'Рейтинг':>8} {'Заказов':>10}")
    print("-" * 65)
    
    for s in suppliers:
        print(f"{s[0]:<25} {s[1]:<20} {s[2]:>8.1f} {s[3]:>10}")

def show_category_report(conn):     ##Функция показывает аналитический отчёт по категориям товаров
    cursor = conn.cursor()
    cursor.execute("""
        SELECT category, COUNT(*) as cnt, SUM(boxes) as total_boxes, SUM(revenue) as total_revenue
        FROM products
        GROUP BY category
        ORDER BY total_revenue DESC
    """)
    categories = cursor.fetchall()
    
    print_section("📊 ОТЧЁТ ПО КАТЕГОРИЯМ")
    print(f"{'Категория':<15} {'Товаров':>8} {'Ящиков':>10} {'Выручка':>18}")
    print("-" * 55)
    
    for c in categories:
        print(f"{c[0]:<15} {c[1]:>8} {c[2]:>10} {c[3]:>17,.0f} руб.")

def show_top_products(conn):       #Функция показывает топ-3 товара по выручке
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name, supplier, revenue 
        FROM products 
        ORDER BY revenue DESC 
        LIMIT 3
    """)
    top = cursor.fetchall()
    
    print_section("🏆 ТОП-3 ТОВАРА ПО ВЫРУЧКЕ")
    for i, p in enumerate(top, 1):
        print(f"  {i}. {p[0]} (поставщик: {p[1]}) — {p[2]:,.0f} руб.")

def show_supplier_stats(conn):        #Функция показывает статистику по выручке каждого поставщика
    cursor = conn.cursor()
    cursor.execute("""
        SELECT supplier, COUNT(*) as cnt, SUM(revenue) as total_revenue
        FROM products
        GROUP BY supplier
        ORDER BY total_revenue DESC
    """)
    stats = cursor.fetchall()
    
    print_section("📈 ВЫРУЧКА ПО ПОСТАВЩИКАМ")
    for s in stats:
        print(f"  {s[0]}: {s[1]} товаров — {s[2]:,.0f} руб.")

def main():                            #Главная функция программы.
    print_header("📦 СКЛАДСКОЙ УЧЁТ ТОВАРОВ 📦")
    
    conn = get_connection()
    create_tables(conn)
    load_demo_data(conn)
    
    # Показываем все отчёты
    show_products_report(conn)
    show_suppliers_report(conn)
    show_category_report(conn)
    show_top_products(conn)
    show_supplier_stats(conn)
    
    print_header("✅ ПРОЕКТ ГОТОВ К ЭКЗАМЕНУ")
    
    conn.close()

if __name__ == "__main__":
    main()