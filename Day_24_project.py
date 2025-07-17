for num in range(1, int(input("pick a number please: "))):
    if num % 2 != 0:     
        print(num, end=" ")



s2 = ['apple', 'strawberry', 'watermelon', 'lemon']
s2_result = [ i.capitalize() for i in s2]
print (s2_result)