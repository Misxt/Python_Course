numbers = [7, 5, 2, 9, 3, 4, 8]
smallNumber = float("inf")
for pos in range (len(numbers)):
    if numbers[pos] < smallNumber:
        smallNumber = numbers[pos]
print(smallNumber)