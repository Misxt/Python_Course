from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        return_list = []
        for i in range(len(arr[:-1])):
            highest_element = self.get_greatest(arr[i+1:])
            return_list.append(highest_element)
        return_list.append(-1)
        return return_list
    
    def get_greatest(self, _list):
        bigNumber = float("-inf")
        for pos in range (len(_list)):
            if _list[pos] > bigNumber:
                bigNumber = _list[pos]
        return bigNumber

"""
Homework
"""

test = Solution()
print(test.get_greatest([15,3,5,17,21,9]))