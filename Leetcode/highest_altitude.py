from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        highest_altitude = 0
        for i in range(len(gain)):
            altitude = altitude + gain[i]
            if altitude > highest_altitude:
                highest_altitude = altitude
        return highest_altitude
    
test = Solution()
print(test.largestAltitude([-4,-3,-2,-1,4,3,2]))