number_of_students = int(input())
student_grades = []
general_counter = 0
scope_counter = 0
original_grade_counter = 0
bonus_grade_counter = 0
changed_grade_counter = 0


class Student:
    def __init__(self):
        self.original_grade = None
        self.bonus_grade = None
        self.final_grade = None
        self.is_original = None

    def calculate_note(self):
        if self.bonus_grade != 10 or self.original_grade == 10 and self.bonus_grade > 0:
            self.final_grade = self.original_grade
            self.is_original = True
        if self.bonus_grade == 10 and self.original_grade != 10:
            self.final_grade = self.original_grade + 2
            self.is_original = False
        if self.final_grade > 10:
            self.final_grade = 10.00


if 0 < number_of_students <= 999:
    while general_counter < number_of_students:
        student = Student()
        student_grades.append(student)
        general_counter += 1

    while scope_counter < number_of_students * 2:
        grade = float(input())
        if scope_counter < number_of_students:
            student_grades[original_grade_counter].original_grade = grade
            original_grade_counter += 1
        else:
            student_grades[bonus_grade_counter].bonus_grade = grade
            bonus_grade_counter += 1
        scope_counter += 1

    # Verify quantity of changed grades
    for x in student_grades:
        x.calculate_note()
        if not x.is_original:
            changed_grade_counter += 1
    print(f'NOTAS ALTERADAS: {changed_grade_counter}')

    for x in student_grades:
        # Index of student grade
        if number_of_students < 10:
            index_counter = f'00{int(student_grades.index(x)) + 1}'
        elif 10 <= number_of_students < 100:
            index_counter = f'0{int(student_grades.index(x)) + 1}'
        elif 100 < number_of_students <= 999:
            index_counter = number_of_students
        else:
            index_counter = 0

        # Generating number pattern
        if x.original_grade < 10:
            x.original_grade = f'0{x.original_grade:.2f}'
        if x.final_grade < 10:
            x.final_grade = f'0{x.final_grade:.2f}'
        if x.final_grade == 10:
            x.final_grade = f'10.00'
        if x.original_grade == 10:
            x.original_grade = f'10.00'


        # Generate template string for printing
        grade_string = f'({index_counter}) original: {x.original_grade} | final: {x.final_grade}'

        if x.is_original:
            print(f'-{grade_string}')
        else:
            print(f'*{grade_string}')
