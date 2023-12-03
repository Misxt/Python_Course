from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        destination_cities = {}
        #Hint: Key and value of a dictionary
        for i in range(len(paths)):
            destination_cities[paths[i][0]] = paths[i][1]
        for key in destination_cities:
            value = destination_cities[key]
            if not destination_cities.get(value):
                return value
