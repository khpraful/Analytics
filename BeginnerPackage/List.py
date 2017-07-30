import random
import os
import sys


#List operations
grocery_list = ['tomatoes', 'potatoes', 'sugar']
juice_list  =['carrot juice', 'orange juice']

print("First item:", grocery_list[0])
grocery_list [0] = "cauliflower"
print("First item:", grocery_list[0])
print(grocery_list[0:3])
combined_list = [grocery_list, juice_list]
print (combined_list)
print (combined_list[0][1])
grocery_list.append("ladyfinger")
grocery_list.insert(2, "onions")
print(grocery_list)
grocery_list.sort()
print(grocery_list)
grocery_list.reverse()
print(grocery_list)
print(len(combined_list))
print(max(combined_list))
print(min(combined_list))
print(len(grocery_list))
print(max(grocery_list))
print(min(grocery_list))

