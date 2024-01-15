number_of_students = int(input())

students = {}

for i in range(number_of_students):
    student_data = input().split()
    name, grade = student_data[0], float(student_data[1])

    if name not in students:
        students[name] = []
    students[name].append(grade)

for name, grades in students.items():
    avg_grade = sum(grades) / len(grades)
    formatted_grades = f'{" ".join([f"{g:.2f}" for g in grades])}'
    print(f"{name} -> {formatted_grades} (avg: {avg_grade:.2f})")