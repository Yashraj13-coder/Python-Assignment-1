#Dictionary & List 
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 88,
    "Eva": 95
}
name = input("Enter the student's name: ")
if name in student_marks:
    print(f"{name}'s marks are: {student_marks[name]}")
else:
    print(f"Student named '{name}' not found in the record.")