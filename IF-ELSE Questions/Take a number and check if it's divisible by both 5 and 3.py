# 6. Take a number and check if it's divisible by both 5 and 3.

num = int(input("Enter a Number: "))

if num % 5 == 0 and num % 3 == 0:
    print("Divisible by Both 5 and 3")
else:
    print("Not Divisible by Both 5 and 3")
