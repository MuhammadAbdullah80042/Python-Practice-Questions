# Q5: Write a function that accepts variable arguments (*args) and returns their sum. ( USED AI )

def sum_args(*args):
    total = 0
    for num in args:
        total += num
    return total