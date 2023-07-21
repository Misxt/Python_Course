class Solution:
    def isPalindrome(self, x: int) -> bool:
        intsplitter = str(x)
        letters_list = []
        for i in range(len(intsplitter)):
            letter = intsplitter[i]
            letters_list.append(letter)
        original_list = letters_list.copy()
        letters_list.reverse()
        if original_list == letters_list:
            return True
        else:
            return False
answer = Solution()
print(answer.isPalindrome(1231))