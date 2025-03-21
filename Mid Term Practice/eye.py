# Define the mapping of words/phrases to their phonetic equivalents
mapping = {
    "at": "@",
    "and": "&",
    "eye": "i",
    "you": "u",
    "are": "r",
    "why": "y",
    "one": "1",
    "won": "1",
    "two": "2",
    "four": "4",
    "for": "4",
    "to": "2",
    "two": "2",
    "too": "2",
    "be": "b",
    "bee": "b",
    "bea": "b",
    "sea": "c",
    "see": "c",
    "oh": "o",
    "owe": "o",
    "are": "r",
}

# Read the number of lines
num_of_lines = int(input())

# Process each line
for _ in range(num_of_lines):
    line = input().strip()
    words = line.split()
    transformed_words = []

    for word in words:
        lower_word = word.lower()
        if lower_word in mapping:
            replacement = mapping[lower_word]
            if word.isupper():
                replacement = replacement.capitalize()
            transformed_words.append(replacement)
        else:
            transformed_words.append(word)
    
    print(" ".join(transformed_words))