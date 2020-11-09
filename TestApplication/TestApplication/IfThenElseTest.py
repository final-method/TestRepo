name = input("Please tell me your name. ")
rawAge = int(input("Please tell me your age. "))

if rawAge >= 21:
    print(name, "Your allowed to come in!")
    print("What would you like to drink?")
    print("I made a change here")
elif rawAge >=18:
    print(name, "Your are allowed to come in!")
    print("However, you are not allowed to drink! Please feel free to enjoy everything else")
else:
    print("Sorry!", name, "Your not old enough")
