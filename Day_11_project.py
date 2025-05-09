num= int(input("Enter any number: "))
Ans = ''  

while num > 0:
    Ans = str(num & 1) + Ans
    num >>= 1
print(Ans)