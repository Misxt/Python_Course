class Solution:
    def countAsterisks(self, s: str) -> int:
        flag = False
        counter = 0
        for i in range(len(s)):
            if s[i] == "|":
                if flag == False:
                    flag = True
                else:
                    flag = False
            if flag == False:
                if s[i] == "*":
                    counter = counter + 1
        return counter