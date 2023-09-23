from typing import List
#Use a dictionary
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        center_dictionary = {}
        center_node = 0
        center_number = 0
        for i in range(len(edges)):
            for r in range(len(edges[i])):
                if edges[i][r] in center_dictionary.keys():
                    center_dictionary[edges[i][r]] = center_dictionary[edges[i][r]] + 1
                else:
                    center_dictionary[edges[i][r]] = 1
        
        for key in center_dictionary:
            if center_dictionary[key] > center_node:
                center_node = key
                center_number = center_dictionary[key]
        return center_node
test = Solution()
print(test.findCenter([[1,2], [3,2], [4,2]]))