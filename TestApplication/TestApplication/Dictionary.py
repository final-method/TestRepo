ages = {"Ben": 35, "Joe": 37, "Sally": 22, "Jeff": 18}

#print(ages.keys())
#x = list(ages.keys())
#print(x[2])

#for key in x:
#    print(key)


#for age in ages:
#    print('The age of', age, 'is', ages[age])

newKey = input('Enter the key you would like to change: ')
newValue = int(input('Enter the new value to add: '))

ages[newKey] = newValue
print(ages)

newKey = input('Enter the new key you would like to add: ')
newValue = int(input('Please enter the new value to add: '))

ages[newKey] = newValue
print(ages)

remKey = input('Enter a key to remove ')
del ages[remKey]
print(ages)