try:
    number = int(input("enter a number: "))
    print("enter number as is" , number)
except ValueError as ex:
    print("excpetion", ex)