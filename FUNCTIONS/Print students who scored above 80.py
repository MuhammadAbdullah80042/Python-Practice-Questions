# Q8: Print students who scored above 80

def a(b):
    for c, d in b.items():
        if d > 80:
            print(c, "scored:", d)

b = {"Alice": 90, "Bob": 75, "Charlie": 85, "David": 60}
a(b)
