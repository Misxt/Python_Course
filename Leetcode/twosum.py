from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range (len(nums)):
        for j in range (len(nums)):
            if i == j:
                continue
            elif nums[i] + nums[j] == target:
                answer = [i, j]
                return answer
            else:
                continue
print(twoSum([1,2,3,4], 5))