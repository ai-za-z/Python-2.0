def count_value_frequency(dictionary, value):
    count = 0
    for key in dictionary:
        if dictionary[key] == value:
            count += 1
    return count

test_dict = {'Codingal': 2, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}
value_to_count = 2
frequency = count_value_frequency(test_dict, value_to_count)

print(f"The frequency of '{value_to_count}' in the dictionary is: {frequency}")