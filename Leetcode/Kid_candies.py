from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        returnlist = []
        greatest_candy = 0
        for i in range(len(candies)):
            if candies[i] > greatest_candy:
                greatest_candy = candies[i]
        for i in range(len(candies)):
            theoreticalcandies = candies[i] + extraCandies
            if theoreticalcandies >= greatest_candy:
                returnlist.append(True)
            else:
                returnlist.append(False)
        return returnlist