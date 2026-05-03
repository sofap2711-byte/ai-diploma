from text_utils import normalize_text, word_count, contains_word
from data_utils import find_by_name, filter_by_value, count_items
from file_utils import save_text, load_text, append_text, count_lines
from csv_utils import save_csv, load_csv, count_csv_rows, sum_column
from json_utils import save_json, load_json, dict_to_json_text


def build_warehouse_report(description, products, suppliers):
    """Формирует отчёт о складе на основе данных"""
    clean_desc = normalize_text(description)
    words = word_count(clean_desc)
    has_urgent = contains_word(clean_desc, "срочно")
    product_count = count_items(products)
    supplier_count = count_items(suppliers)

    report = {
        "clean_description": clean_desc,
        "word_count": words,
        "has_urgent": has_urgent,
        "product_count": product_count,
        "supplier_count": supplier_count
    }

    return report


def run_warehouse_scenario():
    
    # ============================================================
    # 1️⃣ ДАННЫЕ О СКЛАДЕ (товары, поставщики, ящики)
    # ============================================================
    
    # 📦 Описание склада
    description = "   Срочно нужно принять товар и обновить остатки на складе   "

    # 🛒 Список товаров на складе
    products = [
        "Ноутбуки",
        "Мыши",
        "Клавиатуры",
        "Мониторы",
        "Наушники"
    ]

    # 🚚 Поставщики с товарами и количеством ящиков
    suppliers = [
        {"name": "ООО ТехноПост", "product": "Ноутбуки", "boxes": 15},
        {"name": "ООО ТехноПост", "product": "Мыши", "boxes": 45},
        {"name": "ИП Иванов", "product": "Клавиатуры", "boxes": 30},
        {"name": "ООО ЭкранПлюс", "product": "Мониторы", "boxes": 12},
        {"name": "ИП Иванов", "product": "Наушники", "boxes": 28},
        {"name": "ООО ТехноПост", "product": "Мониторы", "boxes": 8}
    ]

    # ============================================================
    # 2️⃣ ИМЕНА ФАЙЛОВ
    # ============================================================
    
    TEXT_FILE = "warehouse_note.txt"
    CSV_FILE = "warehouse_products.csv"
    JSON_FILE = "warehouse_config.json"

    # ============================================================
    # 3️⃣ ДАННЫЕ ДЛЯ CSV (остатки товаров)
    # ============================================================
    
    rows = [
        ["товар", "остаток_ящиков", "поставщик"],
        ["Ноутбуки", 15, "ООО ТехноПост"],
        ["Мыши", 45, "ООО ТехноПост"],
        ["Клавиатуры", 30, "ИП Иванов"],
        ["Мониторы", 20, "ООО ЭкранПлюс"],
        ["Наушники", 28, "ИП Иванов"]
    ]

    # ============================================================
    # 4️⃣ ОСНОВНОЙ КОД (НЕ МЕНЯТЬ)
    # ============================================================
    
    # Формируем отчёт
    report = build_warehouse_report(description, products, suppliers)

    # Поиск поставщика по имени
    found_supplier = find_by_name(suppliers, "ООО ТехноПост")
    
    # Фильтрация по товару
    laptop_suppliers = filter_by_value(suppliers, "product", "Ноутбуки")

    # Сохраняем описание в текстовый файл
    save_text(TEXT_FILE, report["clean_description"])
    append_text(TEXT_FILE, "Отчёт по складу сформирован автоматически.")

    loaded_note = load_text(TEXT_FILE)
    note_lines = count_lines(TEXT_FILE)

    # Сохраняем CSV
    save_csv(CSV_FILE, rows)
    loaded_csv = load_csv(CSV_FILE)
    csv_rows = count_csv_rows(CSV_FILE)
    
    # Суммируем остатки (второй столбец — количество ящиков)
    total_boxes = sum_column(CSV_FILE, 1)

    # Сохраняем JSON-конфигурацию
    warehouse_config = {
        "warehouse_name": "Центральный склад",
        "total_products": report["product_count"],
        "total_suppliers": report["supplier_count"],
        "total_boxes_on_hand": total_boxes,
        "note_lines": note_lines,
        "csv_rows": csv_rows
    }

    save_json(JSON_FILE, warehouse_config)
    loaded_config = load_json(JSON_FILE)
    config_text = dict_to_json_text(loaded_config)

    # ============================================================
    # 5️⃣ ВЫВОД РЕЗУЛЬТАТА
    # ============================================================
    
    print("=== СКЛАДСКОЙ УЧЁТ ТОВАРОВ ===")
    print()
    print("📦 1. ИНФОРМАЦИЯ О СКЛАДЕ:")
    print("Очищенное описание:", report["clean_description"])
    print("Количество слов в описании:", report["word_count"])
    print("Есть слово 'срочно':", report["has_urgent"])
    print()

    print("🛒 2. СПИСОК ТОВАРОВ НА СКЛАДЕ:")
    print("Товары:", products)
    print("Количество видов товаров:", report["product_count"])
    print()

    print("🚚 3. ПОСТАВЩИКИ:")
    print("Найден поставщик 'ООО ТехноПост':", found_supplier)
    print("Поставщики ноутбуков:", laptop_suppliers)
    print("Всего поставщиков:", report["supplier_count"])
    print()

    print("📄 4. ТЕКСТОВЫЙ ФАЙЛ:", TEXT_FILE)
    print("Содержимое:")
    print(loaded_note)
    print("Количество строк:", note_lines)
    print()

    print("📊 5. CSV ФАЙЛ:", CSV_FILE)
    print("Таблица остатков:")
    for row in loaded_csv:
        print(f"   {row}")
    print(f"Всего строк в таблице (с заголовком): {csv_rows}")
    print(f"Общее количество ящиков на складе: {total_boxes}")
    print()

    print("🔧 6. JSON КОНФИГУРАЦИЯ:")
    print("Сохранённая конфигурация:", loaded_config)
    print("JSON-текст:")
    print(config_text)
    print()

    print("✅ Складской учёт успешно запущен!")
    print()
    print("📁 Созданные файлы:")
    print(f"   - {TEXT_FILE}")
    print(f"   - {CSV_FILE}")
    print(f"   - {JSON_FILE}")


def main():
    run_warehouse_scenario()


if __name__ == "__main__":
    main()