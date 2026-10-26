students = {
    "Rahul": 85,
    "pritam": 45,
    "subhajit": 72,
    "sudipto": 38,
    "akash": 60
}

print("Student Names and Marks:")

for name, marks in students.items():
    print(name, ":", marks)

print("\nStudents who scored 50 or above:")

for name, marks in students.items():
    if marks >= 50:
        print(name)

highest = max(students.values())
print("\nHighest Mark:", highest)