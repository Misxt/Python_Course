from copy import deepcopy
class Solution:
    def maximum69Number (self, num: int) -> int:
        largest_number = num
        num = str(num)
        num = list(num)
        for i in range(len(num)):
            test_number = deepcopy(num)
            changing_number = 0
            if num[i] == "6":
                changing_number = "9"
            elif num[i] == "9":
                changing_number = "6"
            test_number[i] = changing_number
            test_number = int("".join(test_number))
            if test_number > largest_number:
                largest_number = test_number
        return largest_number
    
test = Solution()
print(test.maximum69Number(66666))