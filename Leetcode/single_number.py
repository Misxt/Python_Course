from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number_checking = None
        for i in range(len(nums)):
            number_checking = nums[i]
            found_flag = False
            for j in range(len(nums)):
                if j != i:
                    if number_checking == nums[j]:
                        found_flag = True
                        break
            if found_flag == False:
                return number_checking
test = Solution()
print(test.singleNumber([1,3,1,4,3]))
#Use Dictionaries with Number:Number of times it appears