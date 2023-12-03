from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return_list = []
        while names != []:
            removing_number = self.tallest_person(names, heights)
            return_list.append(names[removing_number])
            names.pop(removing_number)
            heights.pop(removing_number)
        return return_list
        
        
    def tallest_person(self, names, heights):
        greatest_number = 0
        removable_number = 0
        for i in range(len(heights)):
            if heights[i] > greatest_number:
                removable_number = i
                greatest_number = heights[i]
        return removable_number
    
solution = Solution()
solution.sortPeople(["Emma", "John", "Mary"], [5, 2, 10])