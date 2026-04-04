
# List Example
fruits = ["apple","orrange","banana"] 

print(fruits)
print(fruits[1])


# defined inbuilt method or functions 

# add new value at the end 
fruits.append("Graps")
print(fruits)

# add value in middle of list
fruits.insert(1,"kiwi")
print(fruits)

# remove value
fruits.remove("apple")
print(fruits)

fruits.pop(2) # Remove banana
print(fruits)

# Remove All value
fruits.clear()
print(fruits)
