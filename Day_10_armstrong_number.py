num = int(input("enter a number: "))
sum = 0
temp = 0
while temp > 0:
    digit = temp % 10
    sum+= digit ** 3
    temp //=10

if num == sum:
    print(num,"it is an Amrstrong number")
else:
    print(num, "it is not an Armstrong number")
