import random
from nltk.corpus import words

english_words = words.words()
random_word = random.choice(english_words)

number_letter_mapping = {
    's': '5',
    't': '7',
    'a': '4',
    'e': '3',
    'i': '1',
    'o': '0',
    'b': '8'
}

number_letters = set(number_letter_mapping.keys())
filtered_words = [
    word for word in english_words if len(word) == 7
    and word[0] in number_letters
    and word[4] in number_letters
    and word[5] in number_letters
    and word[6] in number_letters
    ]

def sanitize_word(word, mapping, positions):
    word_list = list(word)
    for pos in positions:
        if word[pos] in mapping:
            word_list[pos] = mapping[word[pos]]
    return ''.join(word_list)

for word in filtered_words:
    sanitized_word = sanitize_word(word, number_letter_mapping, [0, 4, 5, 6])

word_count = len(filtered_words)
print(word_count)

with open("output.txt", "w") as file:
    # Process and write all words to the file
    for word in filtered_words:
        sanitized_word = sanitize_word(word, number_letter_mapping, [0, 4, 5, 6])
        file.write(f"Original word: {word}\nLicense Plate: {sanitized_word}\n\n")

print("Output written to output.txt")