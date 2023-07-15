def inverse_dictionary(olddic):
    newdictionary = {}
    for key in olddic:
        print(key, olddic[key])
        newdictionary[olddic[key]] = key
    print(olddic)
    print(newdictionary)
dic1 = {"Hello":5, "What":6, "Huh":5}
inverse_dictionary(dic1)
# dic2 = {}
# dic2["Ramen"] = 10
# print(dic2)