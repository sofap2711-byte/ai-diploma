def normalize_text(text):
    """Очищает текст: убирает пробелы по краям и приводит к нижнему регистру"""
    return text.strip().lower()

def word_count(text):
    """Считает количество слов в тексте"""
    return len(text.split())

def contains_word(text, word):
    """Проверяет, содержится ли слово в тексте"""
    return word.lower() in text.lower()