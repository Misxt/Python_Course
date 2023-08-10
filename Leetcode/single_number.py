from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        found_numbers = {}
        for i in range(len(nums)):
            if nums[i] in found_numbers:
                found_numbers[nums[i]] = found_numbers[nums[i]] + 1
            else:
                found_numbers[nums[i]] = 1
        for key in found_numbers:
            if found_numbers[key] == 1:
                return key
test = Solution()
print(test.singleNumber([1,3,1,4,3]))
#Use Dictionaries with Number:Number of times it appears