print("Select your ride: ")
print("1. Bike")
print("2. Car")
choice = (input("enter your choice: "))

if( choice==1 ):
    print("1.Road Bike\n")
    print("2. Mountain Bike\n")
    choice2 = (input("enter your choice"))
    if choice2== 1:
        print("you selected Road Bike")
    else:
        print("You have selected Mountain Bike")
elif( choice== 2 ):
    print("what type of car")
    print("1.Nissan")
    print("2.Volkswagon")
    choice3 = (input("enter your choice"))
    if choice3== 1:
        print("you have selected Nissan")
    else:
        print("you have selected Volkswagon")
else:
    print("WRONG CHOICE!")