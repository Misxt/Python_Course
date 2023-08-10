class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        highest_wealth = 0
        for i in range(len(accounts)):
            accumulator = 0
            for j in range(len(accounts[i])):
                accumulator = accumulator + accounts[i][j]
            if accumulator > highest_wealth:
                highest_wealth = accumulator
        return highest_wealth