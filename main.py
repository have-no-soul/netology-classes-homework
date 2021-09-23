class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
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


# some_reviewer = Reviewer('Mary', 'Jane')
# print(some_reviewer)
# print()
#
# some_lecturer = Lecturer('Tony', 'Stark')
# some_lecturer.grades = {'Python': 9, 'Git': 6, 'Java': 8}
# print(some_lecturer)
# print()

# Экземпляры студентов
student_1 = Student('Peter', 'Parker', 'male')
student_1.grades = {'Python': 8, 'Git': 9, 'Java': 6, 'React': 7}
student_1.courses_in_progress = ['Python', 'Git']
student_1.finished_courses = ['Java', 'React']

student_2 = Student('Harry', 'Osborn', 'male')
student_2.grades = {'Python': 6, 'Java': 8, 'React': 10}
student_2.courses_in_progress = ['Python']
student_2.finished_courses = ['React']

# Экземпляры лекторов
lecturer_1 = Lecturer('Tony', 'Stark')
lecturer_1.courses_attached = ['Python', 'Git']
lecturer_1.grades = {'Python': 9, 'Git': 6}

lecturer_2 = Lecturer('Steven', 'Rogers')
lecturer_2.courses_attached = ['React']
lecturer_2.grades = {'React': 8}


students_list = [student_1, student_2]
lecturers_list = [lecturer_1, lecturer_2]

print(students_list[1].grades)


# def students_avg_grades(students_list, course_name):
    # for i in students_list:
    #     if course_name in list(students_list(i).grades):


# print(students_avg_grades(students_list, 'Git'))