class Solution:
    def isHappy(self, n: int) -> bool:
        used_numbers = []
        while n != 1:
            square_list = self.number_splitter(n)
            n = 0
            for i in range(len(square_list)):
                n = n + (square_list[i]**2)
            if n in used_numbers:
                return False
            else:
                used_numbers.append(n)
        return True

    def number_splitter(self, input:int):
        #output_list = list(map(int, str(input[0]))) Use only if loop is too slow
        input_str = str(input)
        return_list = []
        for char in input_str:
            return_list.append(int(char))
        return return_list
    
solution = Solution()
print(solution.isHappy(19))