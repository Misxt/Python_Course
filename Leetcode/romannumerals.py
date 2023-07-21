class Solution:
    def romanToInt(self, s: str) -> int:
        accumulator = 0
        roman_numerals = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        for i in range(len(s)-1):
            if roman_numerals[s[i]] < roman_numerals[s[i+1]]:
                accumulator = accumulator - roman_numerals[s[i]]
            else:
                accumulator = accumulator + roman_numerals[s[i]]
        return accumulator + roman_numerals[s[-1]]
test = Solution()
test.romanToInt("MMDCLX")

