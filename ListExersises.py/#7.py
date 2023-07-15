names = ["Hello", "Watch", "Hello", "Hello"]
# pos_to_delete = []
# Duplicate = ""
# for x in range (len(List)):
#     for y in range (len(List)):
#         if List[x] == List[y] and x != y and y not in pos_to_delete:
#             pos_to_delete.append(y)
# print(List, pos_to_delete)
# for pos in range (len(pos_to_delete)):
#     List.pop(pos_to_delete[pos])
# print(List)

# new_names = []
# for pos in range (len(names)):
#     if names[pos] not in new_names:
#         new_names.append(names[pos])
# print(new_names)

names = set(names)
names = list(names)
print(names)
