assortedChaos = ["a", "ab", "aba", "cbc"]
numberOfTrue = 0
for pos in range (len(assortedChaos)):
    if len(assortedChaos[pos]) >= 2:
        #if assortedChaos[pos][0] == assortedChaos[pos][len(assortedChaos[pos])-1]:
        if assortedChaos[pos][0] == assortedChaos[pos][-1]:
            numberOfTrue = numberOfTrue+1
print(numberOfTrue)