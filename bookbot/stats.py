def get_book_text(filepath):
    with open(filepath, encoding='utf-8') as f:
        text = f.read()
    return text

def word_count(book_text):
    return len(book_text.split())

def count_letters(book_text):
    letter_count = 0
    for char in book_text:
        if char.isalpha():
            letter_count += 1
    return letter_count

def character_count(book_text):
    character_count = {}
    book_text = book_text.lower()
    for char in book_text:
        if not char.isalpha():
            continue
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def sort_on_num(item_dict):
    return item_dict["num"]

def get_sorted_character_counts(character_count_dict):
    sorted_list = []
    for char, count in character_count_dict.items():
        item_dict = {"char": char, "num": count}
        sorted_list.append(item_dict)
    sorted_list.sort(reverse=True, key=sort_on_num)
    return sorted_list
