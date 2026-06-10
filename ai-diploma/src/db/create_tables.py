def create_products_table(connection):
    """Создаёт таблицу products для складского учёта"""

    # connection — это открытое подключение к файлу БД
    # .cursor() создаёт из него курсор — специальный объект для выполнения SQL-команд
    cursor = connection.cursor()

    # .execute(...) говорит курсору: «выполни эту SQL-команду»
    # Внутри скобок — многострочная строка с запросом CREATE TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (   -- IF NOT EXISTS: создаём таблицу, только если её ещё нет
        id INTEGER PRIMARY KEY AUTOINCREMENT,   -- id будет сам увеличиваться при каждой вставке
        name TEXT,          -- название товара, текст
        supplier TEXT,      -- название поставщика, текст
        category TEXT,      -- категория товара, текст
        boxes INTEGER,      -- количество коробок, целое число
        price_per_box REAL, -- цена за коробку, число с дробной частью
        revenue REAL        -- выручка, тоже число с дробью
    )
    """)

    # commit() сохраняет изменения в файл БД — без этого таблица не запишется
    connection.commit()

def create_suppliers_table(connection):
    """Создаёт таблицу suppliers (поставщики)"""

    # suppliers — это таблица поставщиков: кто поставляет товары на склад
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS suppliers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,   -- уникальный номер поставщика
        name TEXT,          -- название компании или ИП
        city TEXT,          -- город, откуда поставщик
        contact TEXT,       -- контакт: email или телефон
        rating REAL,        -- рейтинг поставщика, например 4.8
        total_orders INTEGER    -- сколько заказов у поставщика
    )
    """)

    connection.commit()

def create_all_tables(connection):
    """Создаёт все таблицы проекта"""

    # Вызываем функции по очереди: сначала products, потом suppliers
    create_products_table(connection)
    create_suppliers_table(connection)
