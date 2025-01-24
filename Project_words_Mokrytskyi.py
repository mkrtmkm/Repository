def input_text(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Файл не знайдено.")
        return ""

def parse_text(text):
    text = text.lower()
    cleaned_text = ""
    for char in text:
        if char.isalnum() or char.isspace():
            cleaned_text += char
    words = cleaned_text.split()
    return words

def count_words(word_list):
    word_counts = {}
    for word in word_list:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def sort(word_counts):
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_words:
        print(f"{word}: {count}")

filename = "input_words.txt"
text = input_text(filename)

if text:
    words = parse_text(text)
    word_counts = count_words(words)
    sort(word_counts)
