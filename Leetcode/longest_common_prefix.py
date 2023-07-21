from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_dict = {}
        for i in range(len(strs)):
            if strs[i][:2] in prefix_dict:
                prefix_dict[strs[i][:2]] = prefix_dict[strs[i][:2]] + 1
            else:
                prefix_dict[strs[i][:2]] = 1
        print(prefix_dict)

test = Solution()
test.longestCommonPrefix(["Float", "Flower", "Happy"])
#Homework: Finish that
        