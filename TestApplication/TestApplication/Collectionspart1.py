names = ["Ben", "Sally", "Amy", "George", "Randy", "Alice"]

# x = len(names) #shows the number of individual items

#print(x)

#x = names.index("George") #Finds items in index.
#print(x)

#for index in range (0, len(names)):  #utilizing indexing and lengths to pull values
 #   print(names[index], "is found at index", index)

#for name in names:  #completes the same as the above however, this looks at the index instead of the len
  #  print(name, 'is found at index', names.index(name))

##for name in names:
    ##print(name)


print(names)

newIndex = int(input('Please enter the index to replace: '))

newName = input('Please enter the name to put in the index: ')

names[newIndex] = newName
print(names)

newName = input('Please enter a new name to add to the list: ')
names.append(newName)
print(names)

newName = input("Please enter the name to remove from the list: ")
names.remove(newName)
print(names)
