def students_list(student_list):
    for student in student_list:
        print(student[0])
    print("Student list printed")

def average_grade(student_list):
    averages = []
    for student in student_list:
        name = student[0]
        grades = student[1:]
        avg = sum(grades) / len(grades)
        averages.append((name, round(avg, 2)))
    print("Average grades:", averages)
    return averages

def best_student(student_list):
    averages = average_grade(student_list)
    best = max(averages, key=lambda x: x[1])
    print("Best student:", best)
    return best

def add_student(student_list, new_student):
    student_list.append(new_student)
    print(f"Student {new_student[0]} added")
    return student_list

def sort_students_by_avg(student_list):
    averages = average_grade(student_list)
    sorted_students = sorted(averages, key=lambda x: x[1], reverse=True)
    print("Sorted students by average:", sorted_students)
    return sorted_students

def update_grade(student_list, name, subject_idx, new_grade):
    for i, student in enumerate(student_list):
        if student[0] == name:
            student_list[i] = student[:subject_idx] + (new_grade,) + student[subject_idx+1:]
            print(f"Updated {name}'s grade in subject {subject_idx} to {new_grade}")
            break
    return student_list


students = [
    ("Adam", 80, 67, 98),
    ("Ewa", 60, 70, 90),
    ("Karol", 40, 50, 60),
    ("Monika", 90, 90, 90),
    ("Jakub", 30, 40, 50), 
    ("Lenka", 70, 80, 90)
]


students_list(students)
average_grade(students)
best_student(students)
new_student = ("Zofia", 88, 78, 92)
add_student(students, new_student)
print(sort_students_by_avg(students))
update_grade(students, "Ewa", 2, 75) 
print(students)