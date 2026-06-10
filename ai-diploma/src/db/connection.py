import sqlite3
from pathlib import Path

def get_connection(db_name="warehouse_project.db"):
    """
    Создаёт подключение к SQLite-базе данных.
    База данных будет храниться в папке data/
    """

    data_dir = Path("data")                 # объект-путь к папке data
    data_dir.mkdir(exist_ok=True)           # если папки data нет — создаём её

    db_path = data_dir / db_name            # склеиваем путь: data/warehouse_project.db

    # sqlite3.connect() открывает (или создаёт) файл БД и возвращает объект connection
    # Через этот объект потом создаём cursor и выполняем SQL
    connection = sqlite3.connect(db_path)
    return connection
