sum = 0
add = -1
while add != 0:
    print('The current sum is:', sum)
    print('How much would you like to add?', end='')
    add = int(input("Type 0 to end the program): "))
    sum = sum + add
