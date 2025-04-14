# 8. Take three numbers and find the largest using if-elif-else.

n1 = int(input("Enter First Number: "))
n2 = int(input("Enter Second Number: "))
n3 = int(input("Enter Third Number: "))

if n1 > n2 and n1 > n3:
    print("Largest Number:", n1)
elif n2 > n1 and n2 > n3:
    print("Largest Number:", n2)
else:
    print("Largest Number:", n3)
