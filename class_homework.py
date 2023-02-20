class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.grades = {}
        self.courses_in_progress = []

    def grade_lecturer(self, lecturer, course, grade):
        if not str(grade).isdigit() or not 0 <= grade <= 10:
            print("Неправильное значение оценки!")
            return
        if not check_isinstance(Student, self, Lecturer, lecturer):
            print("Оценка невозможна")
            return
        if course in lecturer.courses_attached and (course in self.courses_in_progress or course in self.finished_courses):
            lecturer.grades_for_lectures[course].append(grade)
        else:
            print("Не найден соответствующиий курс, оценка не выставлена")

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'\
               f'Средняя оценка за домашние задания: {self.count_average_student_grades()}\n' \
               f'Курсы в процессе: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}\n'

    def add_course(self, course):
        self.courses_in_progress.append(course)
        self.grades[course] = []

    def count_average_student_grades(self):
        return count_dict_average(self.grades)

    def __lt__(self, other):
        return self.count_average_student_grades() < other.count_average_student_grades()

    def __le__(self, other):
        return self.count_average_student_grades() <= other.count_average_student_grades()

    def __eq__(self, other):
        return self.count_average_student_grades() == other.count_average_student_grades()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_for_lectures = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.count_average_lecturer_grade()}\n'

    def count_average_lecturer_grade(self):
        return count_dict_average(self.grades_for_lectures)

    def add_course(self, course_name):
        self.courses_attached.append(course_name)
        self.grades_for_lectures[course_name] = []

    def __lt__(self, other):
        return self.count_average_lecturer_grade() < other.count_average_lecturer_grade()

    def __le__(self, other):
        return self.count_average_lecturer_grade() <= other.count_average_lecturer_grade()

    def __eq__(self, other):
        return self.count_average_lecturer_grade() == other.count_average_lecturer_grade()

class Reviewer(Mentor):
    def put_mark(self, student_to_grade, course, grade):
        if not check_isinstance(Reviewer, self, Student, student_to_grade):
            print("Оценка невозможна!")
            return
        if course in student_to_grade.courses_in_progress and course in self.courses_attached:
            student_to_grade.grades[course].append(grade)
        else:
            print("Не найден соответствующий курс, оценка не выставлена!")

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'

def check_isinstance(first_class, first_object, second_class, second_object):
    return isinstance(first_object, first_class) and isinstance(second_object, second_class)

def count_dict_average(dictionary):
    all_values = sum(dictionary.values(), [])
    return sum(all_values) / len(all_values)

def count_students_course_average(course, students_list):
    all_values = []
    for student in students_list:
        if not (course in student.courses_in_progress or course in student.finished_courses):
            return "Не все студенты проходят данный курс"
        else:
            all_values += student.grades[course]
    return sum(all_values) / len(all_values)

def count_lecturers_course_average(course, lecturer_list):
    all_values = []
    for lecturer in lecturer_list:
        if not (course in lecturer.courses_attached):
            return "Не все лекторы прикреплены к курсу"
        else:
            all_values += lecturer.grades_for_lectures[course]
    return sum(all_values) / len(all_values)

lect = Lecturer('Van', 'Darkholm')
lect.add_course('Best Course')
lect.add_course('Worst Course')
lect2 = Lecturer('Billy', 'Herrington')
lect2.add_course('Best Course')
rev = Reviewer('Chuck', 'Norris')
rev.courses_attached += ['Best Course', 'Worst Course']
std = Student('Fyva', 'Itsuken', 'man')
std.add_course('Worst Course')
std.add_course('Best Course')
std.grade_lecturer(lect, 'Best Course', 4)
std.grade_lecturer(lect, 'Best Course', 9)
std.grade_lecturer(lect, 'Worst Course', 8)
std.grade_lecturer(lect2, 'Best Course', 10)
rev.put_mark(std, 'Best Course', 4)
rev.put_mark(std, 'Worst Course', 6)
std2 = Student('Oldja', 'Poiuyt', 'helicopter')
std2.add_course('Best Course')
rev.put_mark(std2, 'Best Course', 9)
rev.put_mark(std2, 'Best Course', 3)

print(std)
print(std2)
print(f'{std < std2}')
print(f'{std >= std2}')
print(f'{std == std2}\n')
print(lect)
print(lect2)
print (f'{lect2 > lect}')
print (f'{lect2 <= lect}')
print (f'{lect2 == lect}\n')
print(rev)
print(count_students_course_average("Best Course", [std, std2]))
print(count_students_course_average("Worst Course", [std, std2]))
print(count_lecturers_course_average("Best Course", [lect, lect2]))
print(count_lecturers_course_average("Worst Course", [lect, lect2]))

