def normalize_text(text):
    return text.strip().lower()

def word_count(text):
    return len(text.split())

def contains_word(text, word):
    return word.lower() in text.lower()
