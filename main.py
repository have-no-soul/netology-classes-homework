class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_avg_grade(self):
        avg_grade = round(sum(self.grades.values()) / len(self.grades.values()), 2)
        return avg_grade

    def __str__(self):
        student_info = f'Имя: {self.name}\n' \
                       f'Фамилия: {self.surname}\n' \
                       f'Средняя оценка за домашние задания: {self.get_avg_grade()}\n' \
                       f'Курсе в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
                       f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return student_info

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.get_avg_grade < other.get_avg_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_avg_grade(self):
        avg_grade = round(sum(self.grades.values()) / len(self.grades.values()), 2)
        return avg_grade

    def __str__(self):
        lecturer_info = f'Имя: {self.name}\n' \
                        f'Фамилия: {self.surname}\n' \
                        f'Средняя оценка за лекции: {self.get_avg_grade()}'
        return lecturer_info


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        reviewer_info = f'Имя: {self.name}\n' \
                        f'Фамилия: {self.surname}'
        return reviewer_info


# Экземпляр Студента-1
student_1 = Student('Peter', 'Parker', 'male')
student_1.courses_in_progress = ['Python', 'Git']
student_1.finished_courses = ['Java', 'React']

# Экземпляр Студента-2
student_2 = Student('Harry', 'Osborn', 'male')
student_2.courses_in_progress = ['Python']
student_2.finished_courses = ['React']

# Экземпляр Лектора-1
lecturer_1 = Lecturer('Tony', 'Stark')
lecturer_1.courses_attached = ['Python', 'Git']

# Экземпляр Лектора-2
lecturer_2 = Lecturer('Steven', 'Rogers')
lecturer_2.courses_attached = ['Python', 'React']

# Экземпляр Ревьюера-1
reviewer_1 = Reviewer('Natasha', 'Romanov')
reviewer_1.courses_attached = ['Python']

# Экземпляр Ревьюера-2
reviewer_2 = Reviewer('Hulk', 'Hogan')
reviewer_2.courses_attached = ['Git', 'React']

# Методы
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Git', 8)

student_2.rate_lecturer(lecturer_2, 'Python', 9)

reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 5)  # Добавляем 2-ое ДЗ по курсу, дабы проверить расчет средней по оценкам курса
reviewer_1.rate_hw(student_2, 'Python', 8)

reviewer_2.rate_hw(student_1, 'Git', 7)

# Две функции
students_list = [student_1, student_2]
lecturers_list = [lecturer_1, lecturer_2]


def students_avg_grades(students_list, course_name):
    counter = 0
    sum_grade = 0
    for student in students_list:
        if course_name in student.grades:
            counter += len(student.grades[course_name])
            sum_grade += sum(student.grades[course_name])

    return round((sum_grade / counter), 2)


print(students_avg_grades(students_list, 'Git'))


def lecturers_avg_grades(lecturers_list, course_name):
    counter = 0
    sum_grade = 0
    for lecturer in lecturers_list:
        if course_name in lecturer.grades:
            counter += len(lecturer.grades[course_name])
            sum_grade += sum(lecturer.grades[course_name])

    return round((sum_grade / counter), 2)


print(lecturers_avg_grades(lecturers_list, 'Git'))
