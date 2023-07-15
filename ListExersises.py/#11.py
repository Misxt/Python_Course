def similarities(l1, l2):
    for x in range (len(l1)):
        for y in range (len(l2)):
         if l1[x] == l2[y] and x != y:
              return(True)
         
List = ["Hello", "Watch", "Hello", "Hello"]
pos_to_delete = ["What", "Hello", "Air", "Oxygen"]
result = similarities(List, pos_to_delete)
print(result)