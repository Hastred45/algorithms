# https://leetcode.com/problems/roman-to-integer/

# class Solution:
def roman_to_int(s: str) -> int:
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for i in range(len(s)):
        # print(roman[s[i]])
        print(i)
        if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
            result -= roman[s[i]]
        else: 
            result += roman[s[i]]
    return result

s = 'III'
# print(roman_to_int(s))
roman_to_int(s)