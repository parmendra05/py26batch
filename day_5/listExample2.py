


nameList = [ "Amrendra","Raju" , "Ramesh", "Amrendra", "Parmendra","Niraj", "Amrendra"]
print(nameList)

# find Index values
print(nameList.index("Ramesh"))

# Second Way
amrendraIndex = nameList.index("Amrendra")
print(amrendraIndex)

#count all value 
print("Countting all the value")
print(len(nameList))

print("check how many duplicate value are present - Amrendra")
print(nameList.count("Amrendra"))

# Sorting the List
nameList.sort()
print(nameList)


# Reverse the List
nameList.reverse()
print(nameList)
