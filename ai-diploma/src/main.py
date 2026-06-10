import sqlite3
from pathlib import Path

def get_connection():
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    db_path = data_dir / "warehouse_project.db"
    return sqlite3.connect(db_path)

def create_tables(conn):
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
    conn.commit()

def add_product(conn, name, supplier, category, boxes, price_per_box):
    cursor = conn.cursor()
    revenue = boxes * price_per_box
    cursor.execute("""
        INSERT INTO products (name, supplier, category, boxes, price_per_box, revenue)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, supplier, category, boxes, price_per_box, revenue))
    conn.commit()

def main():
    conn = get_connection()
    create_tables(conn)
    
    # Очищаем и добавляем данные
    conn.execute("DELETE FROM products")
    
    products = [
        ("Ноутбуки", "ООО ТехноПост", "Техника", 15, 70000.0),
        ("Мыши", "ООО ТехноПост", "Техника", 45, 1500.0),
        ("Клавиатуры", "ИП Иванов", "Техника", 30, 3500.0),
    ]
    
    for p in products:
        add_product(conn, p[0], p[1], p[2], p[3], p[4])
    
    # Выводим данные
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    print("\nТовары на складе:")
    for row in cursor.fetchall():
        print(f"  {row[1]} | {row[2]} | {row[4]} ящиков | {row[6]:,.2f} руб.")
    
    conn.close()
    print("\n✅ Проект готов к показу!")

if __name__ == "__main__":
    main()