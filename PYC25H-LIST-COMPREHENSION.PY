word_list = ["apple", "banana", "kiwi", "grapefruit", "orange", "fig"]

# List comprehension to get words longer than 5 characters and convert to uppercase
long_words_uppercase = [word.upper() for word in word_list if len(word) > 5]

print(long_words_uppercase)  # Output: ['BANANA', 'GRAPEFRUIT', 'ORANGE']