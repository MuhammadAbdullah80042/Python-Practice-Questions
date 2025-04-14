# 4. Check whether a year is a leap year or not.
a = int(input("Enter a Year: "))

if (a % 4 == 0 and a % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")