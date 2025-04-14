# Q6: Find the largest number in a list using a for loop. (USED AI)

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest number:", largest)
