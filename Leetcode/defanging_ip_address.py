class Solution:
    def defangIPaddr(self, address: str) -> str:
        # address_list = list(address)
        # for i in range(len(address_list)):
        #     if address_list[i] == ".":
        #         address_list[i] = "[.]"
        # return ''.join(address_list)
        return address.replace(".", "[.]")
    
test = Solution()
print(test.defangIPaddr("12.2.34.56.7.8"))