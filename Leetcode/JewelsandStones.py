class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # jewels_list = list(jewels)
        # stones_list = list(stones)
        # accumulator = 0
        # for i in range(len(stones_list)):
        #     for j in range(len(jewels_list)):
        #         if stones_list[i] == jewels_list[j]:
        #             accumulator = accumulator + 1
        # return accumulator

        jewels_dict = {}
        accumulator = 0

        jewels_list = list(jewels)
        stones_list = list(stones)

        for i in range(len(jewels_list)):
            jewels_dict[jewels_list[i]] = None

        for i in range(len(stones_list)):
            if stones_list[i] in jewels_dict:
                accumulator = accumulator + 1
        
        return accumulator


        #Homework