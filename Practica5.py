a = int(input("Enter the first number"))
b = int(input("Enter the  second number"))
if a > b:
    for i in range(b,a+1):
        if i % 2 != 0:
            print(i)
else:
    for i in range(a,b+1):
        print(i)
