from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_dict = {}
        largest_prefix = ""
        largest_prefix_count = 0
        for i in range(len(strs)):
            if strs[i][:2] in prefix_dict:
                prefix_dict[strs[i][:2]] = prefix_dict[strs[i][:2]] + 1
            else:
                prefix_dict[strs[i][:2]] = 1
        for key in prefix_dict:
            if prefix_dict[key] > largest_prefix_count:
                largest_prefix = key
                largest_prefix_count = prefix_dict[key]
            elif prefix_dict[key] == largest_prefix_count:
                largest_prefix = ""

        return largest_prefix

test = Solution()
test.longestCommonPrefix(["Float", "Flower", "Happy"])
#Homework: Finish that
        