"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_roman(self, number: int) -> str:
        text_number_roman_dict = {
            'I': 1,
            'V': 5,
            'IX':9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM':900,
            'M': 1000
        }

        if number < 0:
            return "number can not less than 0"
        
        sorted_roman_symbols = sorted(text_number_roman_dict, key=text_number_roman_dict.get, reverse=True)
    
        roman_num = ''
        for symbol in sorted_roman_symbols:
            while number >= text_number_roman_dict[symbol]:
                print(f"number{number}, symb{text_number_roman_dict[symbol]}")
                roman_num += symbol
                print('rom_num', roman_num)
                number -= text_number_roman_dict[symbol]
        
        return roman_num

print(Solution().number_to_roman(954))
