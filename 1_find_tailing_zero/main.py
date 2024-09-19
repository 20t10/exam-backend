"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        if(number < 0):
            return str("number can not be negative")

        count = 0
        while(number >= 5):
            number //= 5
            count += number

        return count


# Driver program
number = 2
print(f"Count of trailing 0s in {number}! is", Solution().find_tailing_zeroes(number))
