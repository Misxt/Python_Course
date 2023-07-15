n = input("Enter n: ")
n = int(n)
accumulator = 1
generator = {}
while accumulator <= n:
    generator[accumulator] = accumulator**2
    accumulator = accumulator+1
for key in generator:
    print(key, generator[key])

