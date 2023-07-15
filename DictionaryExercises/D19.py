dic1 = {"a":5, "b":5, "c":5}
dic2 = {"a":5, "b":5, "c":5}
for key in dic2:
    if key in dic1:
        dic2[key] = dic2[key] + dic1[key]
    else:
        pass
print(dic2)