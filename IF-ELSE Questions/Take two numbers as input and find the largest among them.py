# 7. Take two numbers as input and find the largest among them.

n1 = int(input("Enter First Number: "))
n2 = int(input("Enter Second Number: "))

if n1 > n2:
    print("Largest Number:", n1)
elif n2 > n1:
    print("Largest Number:", n2)
else:
    print("Both Numbers are Equal")