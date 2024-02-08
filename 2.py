student_scores = {
     "Lindell": [85, 90, 92],
     "Gayle": [90, 99, 97],
     "Azy": [92, 96, 98],
}
     
# lindell_grades = student_scores['Lindell']

# print(lindell_grades)

# for grade in lindell_grades:
#    print(grade + grade)

student_grades = [student_scores["Lindell"],
student_scores["Gayle"],
student_scores["Azy"]
] 

for student, grades in student_scores.items():
     print(student)
     for grade in grades:
         print(f'{student}',grade)   