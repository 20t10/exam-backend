"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_textt: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        num_textt = ""
        num_list ={"1": "หนึ่ง'", "2": "สอง", "3": "สาม", "4": "สี่", "5": "ห้า", "6": "หก", "7": "เจ็ด", "8": "แปด", "9": "เก้า"}
        digits_list =  ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]
        new_dict = {}
        result = []
        num_str = str(number)  
        length = len(num_str)  
        num_str = str(number)
        length = len(num_str)
        result = []

        for i, digit in enumerate(num_str):
            position = length - i - 1
            if digit == "0":
                continue

            if position == 0 and digit == "1" and i > 0 and num_str[i-1] != "0":
                result.append("เอ็ด")
            elif position == 1 and digit == "2":
                result.append("ยี่สิบ")
            elif position == 1 and digit == "1" and i + 1 < length and num_str[i+1] == "1":
                result.append("สิบเอ็ด")
            elif position == 1 and digit == "1":
                result.append("สิบ")
            else:
                result.append(num_list[digit])

            if position > 0:
                result.append(digits_list[position])

        return ''.join(result)
    


print(Solution().number_to_thai(5431111))