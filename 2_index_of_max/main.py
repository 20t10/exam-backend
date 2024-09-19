"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list) -> int | str:
        max_number = 0
        max_index = 0
        for i, number in enumerate(numbers):
            if number > max_number:
                max_number = number
                max_index = i
        return max_index

print(Solution().find_max_index([1,2,1,3,5,6,4,7,999,10]))