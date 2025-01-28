import re

def parse_and_clean_text(input_file, output_file):
    # Зчитування тексту з файлу
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Обробка тексту: видалення непотрібних символів і перетворення на слова
    text = text.lower()
    clean_text = re.sub(r'[^a-zа-яіїєґ\s]', '', text)
    words = clean_text.split()

    # Запис списку слів у файл
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(words))

# Виконання програми
if __name__ == "__main__":
    parse_and_clean_text('input_words.txt', 'words.txt')
