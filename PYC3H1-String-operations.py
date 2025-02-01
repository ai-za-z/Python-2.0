str_to_check = "I am a student"

# 1. Count the number of characters
print(f"The number of characters in the sentence above is: {len(str_to_check)}")

# 2. Print the 4th character of the sentence
print(f"The 4th character of the sentence is: {str_to_check[3]}")

# 3. Reverse the sentence
print(f"The sentence in reverse is: {str_to_check[::-1]}")

# 4. Convert the sentence to uppercase
print(f"The sentence in uppercase is: {str_to_check.upper()}")

# 5. Count the number of words
word_count = len(str_to_check.split())
print(f"The number of words in the sentence is: {word_count}")

# 6. Replace 'student' with 'learner'
new_sentence = str_to_check.replace("student", "learner")
print(f"Sentence after replacement: {new_sentence}")

# 7. Check if the sentence starts with "I"
starts_with_I = str_to_check.startswith("I")
print(f"Does the sentence start with 'I'? {'Yes' if starts_with_I else 'No'}")
