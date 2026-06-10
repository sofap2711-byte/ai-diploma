import sqlite3

# Подключаемся к базе
conn = sqlite3.connect("data/warehouse_project.db")
cursor = conn.cursor()

# Показываем все таблицы
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

print("=" * 50)
print("БАЗА ДАННЫХ: warehouse_project.db")
print("=" * 50)

for table in tables:
    table_name = table[0]
    print(f"\n📁 Таблица: {table_name}")
    print("-" * 30)
    
    # Получаем данные из таблицы
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    
    # Получаем названия колонок
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [col[1] for col in cursor.fetchall()]
    
    # Выводим колонки
    print(" | ".join(columns))
    print("-" * 30)
    
    # Выводим данные
    for row in rows:
        print(row)
    print(f"Всего записей: {len(rows)}")

conn.close()
print("\n✅ Готово!")