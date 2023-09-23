class Solution:
    def finalString(self, s: str) -> str:
        letter_list = list(s)
        final_product = ""
        for i in range(len(letter_list)):
            if letter_list[i] == "i":
                final_product = final_product [::-1]
            else:
                final_product = final_product + letter_list[i]
        return final_product


