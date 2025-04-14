# Q4: Write a function to calculate the factorial of a number.

def factorial(n):
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)