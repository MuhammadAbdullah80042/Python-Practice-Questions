# Q7: Write a function to check if a string is a palindrome. (USED AI)

def is_palindrome(s):
    return s == s[::-1]

# Q8: Write a function that accepts a dictionary of student names and marks, then prints students who scored above 80.

def print_top_students(student_marks):
    for name, marks in student_marks.items():
        if marks > 80:
            print("Student:", name, "Marks:", marks)