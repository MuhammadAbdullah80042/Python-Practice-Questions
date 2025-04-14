# Q4: Print a multiplication table of a given number using a for loop. (USED AI)

number = int(input("Enter a Number for Multiplication Table: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")