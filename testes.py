student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

def calculate_grade(score):
    if score > 90:
        return 'Outstanding'
    elif score > 80:
        return 'Exceeds Expectations'
    elif score > 70:
        return 'Acceptable'
    else:
        return 'Fail'

student_grades = dict()
for name, score in student_scores.items():
    student_grades[name] = calculate_grade(score)

print(student_grades)