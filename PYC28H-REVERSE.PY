class StringReverse:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_words(self):
        words = self.input_string.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

# Example Usage
input_str = "Write a Python class to reverse a string word by word"
reverser = StringReverse(input_str)
reversed_str = reverser.reverse_words()
print(reversed_str)