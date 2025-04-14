# Q8: Reverse a given string using a while loop.

s = input("Enter a String to Reverse: ")
reversed_str = ""
index = len(s) - 1
while index >= 0:
    reversed_str += s[index]
    index -= 1
print("Reversed String:", reversed_str)
