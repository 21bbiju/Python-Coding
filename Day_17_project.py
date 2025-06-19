
age = int(input("enter age: "))
    
if age % 2 == 0:
        print("even")
else:
        print("Odd")
try:

    if(age<=1):
        raise ValueError 
    else:
        print("the age is valid")
        
except ValueError:
   print("The age is not valid")


