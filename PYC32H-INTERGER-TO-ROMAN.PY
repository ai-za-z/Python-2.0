class IntegerToRoman:
    def __init__(self, num):
        self.num = num
    
    def convert_to_roman(self):
        roman_numerals = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        result = ""
        num = self.num
        
        for value, symbol in roman_numerals:
            while num >= value:
                result += symbol
                num -= value
        
        return result

# Example usage:
number = int(input("Enter an integer: "))
converter = IntegerToRoman(number)
print("Roman numeral:", converter.convert_to_roman())
