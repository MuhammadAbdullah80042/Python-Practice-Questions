# Q5: Count how many vowels are in a given string using a for loop.

a = input("Enter a String: ")
b = "aeiouAEIOU"
c = 0
for char in b:
    if char in b:
        c += 1
print("Total vowels:", c)