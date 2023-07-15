menu = {"Fish":5,"Pizza":1.50,"Ice_Cream":2}#Key : Value
print(menu["Fish"]) #Prints the value associated with fish
for key in menu:
    print(key, menu[key]) #Prints everything in a dictionary
menu.pop("Fish") #Takes away a value
print(menu)
menu["Ramen"] = 1 #Adds a value and key
print(menu)
menu["Ramen"] = 14 #Changes a value
print(menu)
# print(menu["Hamburglar"])
if "Hamburglar" in menu: #Sees if something is a key of that dictionary
    print("Yes")
else:
    print("No")