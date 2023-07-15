numbers = [7, 5, 2, 9, 3, 4, 8]
bigNumber = float("-inf")
for pos in range (len(numbers)):
    if numbers[pos] > bigNumber:
        bigNumber = numbers[pos]
print(bigNumber)