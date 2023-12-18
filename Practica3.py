a = int(input("Enter the first number"))
b = int(input("Enter the  second number"))
for i in range (a, b + 1):
    if (i % 2 == 0): #Если остаток деления на 2  равен 0 то операция выполняется 
        print(i)