class Student:
    def __init__(self, name, surname, gender="unknown_gender"):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.mean_grade()} \n'+\
        f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res
 

    def mean_grade(self):
        '''Средняя оценка за ДР по всем курсам'''
        all_grades = []
        for vals in list(self.grades.values()):
            all_grades += vals

        if len(all_grades) > 0:
            return sum(all_grades)/len(all_grades)  # Возвращаем среднюю оценку по всем курсам
        else:
            return 0


    def add_course_progress(self, course_name):
        if isinstance(course_name, list):
            self.courses_in_progress.extend(course_name)   
        else:
            self.courses_in_progress.append(course_name)   


    def add_course_finished(self, course_name):
        if course_name in self.courses_in_progress:
            self.courses_in_progress.remove(course_name)
        self.finished_courses.append(course_name)   


    def rate_lector(self, lector, course, grade):
        '''Выставление оценки лектору'''
        if course in (self.finished_courses + self.courses_in_progress):
            if isinstance(lector, Lecturer) and course in lector.courses_attached:
                lector.grades.setdefault(course, [])
                lector.grades[course] += [grade]
        else:
            print('Ошибка')


    def __lt__(self, other):
        '''Сравнение: меньше==true'''
        if isinstance(other, Student):
            return self.mean_grade() < other.mean_grade()
        else:
            return False



     
class Mentor:
    '''Base class for Lecturer and Reviewer'''

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def add_course(self, course_name):
        self.courses_attached.append(course_name)



class Lecturer(Mentor):
    '''Лектор'''

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.mean_grade()}'
        return res


    def mean_grade(self):
        '''Средняя оценка лектора'''
        all_grades = []
        for vals in list(self.grades.values()):
            all_grades += vals

        if len(all_grades) > 0:
            return sum(all_grades)/len(all_grades)  
        else:
            return 0



    def __lt__(self, lector):
        '''Сравнение: меньше==true'''
        if isinstance(lector, Lecturer):
            return self.mean_grade() < lector.mean_grade()
        else:
            return False




class Reviewer(Mentor):
    '''Проверяющий преподаватель'''

    def rate_hw(self, student, course, grade):
        '''Выставление оценок студентам'''
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка')


    def __str__(self):# -> str:
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res



best_student = Student('Джон', 'Смитт', 'муж')
best_student.add_course_progress('Основы программирования')  # Добавление строки с названием курса
best_student.add_course_progress(['Python', 'Git', 'Kotlin'])  # Добавление списка курсов
best_student.add_course_progress('SuperProgrammer')
best_student.add_course_finished('Basic')  # Завершенный курс
best_student.add_course_finished('Основы программирования')  # Завершенный, должен удалиться из изучаемых курсов
# print(best_student)
# print()

bad_student = Student('Вася', 'Пупкин')
bad_student.add_course_progress(['Python', 'Git', 'Basic'])
bad_student.add_course_finished('Основы программирования')
 
cool_mentor = Lecturer('Иван', 'Петрович')
cool_mentor.courses_attached += ['Python', 'Kotlin', 'SuperProgrammer']

any_mentor = Lecturer('Петр', 'Иванович')
any_mentor.courses_attached += ['Git', 'Основы программирования', 'Basic']

first_reviewer = Reviewer('Анна', 'Сергеевна')
first_reviewer.courses_attached += ['Git', 'Основы программирования', 'SuperProgrammer']

smart_reviewer = Reviewer('Николай', 'Степанович')
smart_reviewer.courses_attached += ['Python', 'Kotlin', 'Basic']




smart_reviewer.rate_hw(best_student, 'Python', 10)
smart_reviewer.rate_hw(best_student, 'Python', 9)
smart_reviewer.rate_hw(best_student, 'Python', 10)

first_reviewer.rate_hw(best_student, 'SuperProgrammer', 8)

smart_reviewer.rate_hw(bad_student, 'Python', 6)
smart_reviewer.rate_hw(bad_student, 'Python', 8)

first_reviewer.rate_hw(bad_student, 'Git', 8)


best_student.rate_lector(cool_mentor, 'Python', 10)
best_student.rate_lector(cool_mentor, 'SuperProgrammer', 8)

#first_reviewer.rate_hw(best_student, 'Kotlin', 10)
 
#print(best_student.grades)

#print(cool_mentor)

print('1.')
print(best_student)
print('\n 2.')
print(bad_student)
print('\n 3.')
print(cool_mentor)
print('\n 4.')
print(any_mentor)
print('\n 5.')
print(first_reviewer)
print('\n 6.')
print(smart_reviewer)

# lect1 = Lecturer('Роман','Катин')
# lect1.grades = {'abc':[10,2], 'cde':[4,6]}

#grades_all = []
# grades_all = [sum(x)/len(x) for x in list(lect1.grades.values())]
# grades_mean = sum(grades_all)/len(grades_all)

# print(grades_all, grades_mean)
# print(lect1)
# print(lect1<cool_mentor)
# print(bad_student)