class Student:
    def __init__(self, name, surname, gender="unknown_gender"):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \
        \nСредняя оценка за домашние задания: {self.mean_grade()} \
        \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \
        \nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res


    def mean_grade(self):
        '''Средняя оценка за ДР по всем курсам'''
        all_grades = [a for val in list(self.grades.values()) for a in val]
        if len(all_grades) > 0:
            return sum(all_grades)/len(all_grades)
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
        if course in (self.finished_courses + self.courses_in_progress) \
        and isinstance(lector, Lecturer) and course in lector.courses_attached:
            lector.grades.setdefault(course, [])
            lector.grades[course] += [grade]
        else:
            print(f'Ошибка: оценка для {lector.surname}, курс "{course}", от студента {self.surname}')


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
        res = f'Имя: {self.name} \nФамилия: {self.surname} \
        \nСредняя оценка за лекции: {self.mean_grade()}'
        return res


    def mean_grade(self):
        '''Средняя оценка лектора'''
        all_grades = [a for val in list(self.grades.values()) for a in val]

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
        if isinstance(student, Student) and course in self.courses_attached \
        and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print(f'Ошибка: оценка ст. {student.surname}, за курс "{course}", пров. {self.surname}')


    def __str__(self):# -> str:
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res



#-------------------------------------------------------------------------------

##def mean_grade_course(student_list, course_name):
##    if not isinstance(student_list, list) or not isinstance(course_name, str):
##        return 0
##    grades = [g for student in student_list  for g in student.grades.get(course_name, [])  if isinstance(student, Student)]
##    print(grades)


def mean_grade_course(person_list, course_name, class_person=Student):
    '''
    Подсчет средней оценки за курс (студенты (по умолч.) или лекторы)
      person_list - список студентов или преподавателей
      course_name - название курса
      class_person - Student или Lecturer
    '''

    if not isinstance(person_list, list) or not isinstance(course_name, str):
        return 0

    # Генератор работает, но нечитаем и не помещается в 80 символов
#    grades = [g for person in person_list  for g in person.grades.get(course_name, [])  if isinstance(person, class_person)]

    grades = []
    for person in person_list:
        if isinstance(person, class_person):
            for grade in person.grades.get(course_name, []):
                grades.append(grade)
#    print(grades)

    if len(grades) > 0:
        return(sum(grades) / len(grades))
    else:
        return 0;



def mean_grade_course_mentors(lector_list, course_name):
    '''
    Подсчет средней оценки за курс только для лекторов
      lector_list - список преподавателей
      course_name - название курса
    '''
    return(mean_grade_course(lector_list, course_name, Lecturer))





#-------------------------------------------------------------------------------

# Заводим хорошего студента
best_student = Student('Джон', 'Смитт', 'муж')
best_student.add_course_progress('Основы программирования')  # Добавление строки с названием курса
best_student.add_course_progress(['Python', 'Git', 'Kotlin'])  # Добавление списка курсов
best_student.add_course_progress('SuperProgrammer')
best_student.add_course_finished('Basic')  # Завершенный курс
best_student.add_course_finished('Основы программирования')  # Завершенный, должен удалиться из изучаемых курсов


# Заводим плохого студента
bad_student = Student('Вася', 'Пупкин')
bad_student.add_course_progress(['Python', 'Git', 'Basic'])
bad_student.add_course_finished('Основы программирования')


# Преподаватели
cool_mentor = Lecturer('Иван', 'Петрович')
cool_mentor.courses_attached += ['Python', 'Kotlin', 'SuperProgrammer']

any_mentor = Lecturer('Петр', 'Иванович')
any_mentor.courses_attached += ['Git', 'Основы программирования', 'Basic']


# Проверяющие
smart_reviewer = Reviewer('Николай', 'Степанович')
smart_reviewer.courses_attached += ['Python', 'Kotlin', 'Basic']

first_reviewer = Reviewer('Анна', 'Сергеевна')
first_reviewer.courses_attached += ['Git', 'Основы программирования', 'SuperProgrammer']




# Выставление оценок студентам
smart_reviewer.rate_hw(best_student, 'Python', 10)
smart_reviewer.rate_hw(best_student, 'Python', 9)
smart_reviewer.rate_hw(best_student, 'Kotlin', 10)
first_reviewer.rate_hw(best_student, 'SuperProgrammer', 8)
smart_reviewer.rate_hw(best_student, 'Basic', 8)  # Должна быть ошибка, курс завершен
first_reviewer.rate_hw(best_student, 'Kotlin', 9)  # Ошибка - не тот проверяющий
print(f'best student: {best_student.grades}')

smart_reviewer.rate_hw(bad_student, 'Python', 6)
smart_reviewer.rate_hw(bad_student, 'Python', 8)
smart_reviewer.rate_hw(bad_student, 'Python', 5)
smart_reviewer.rate_hw(bad_student, 'Basic', 10)
first_reviewer.rate_hw(bad_student, 'Git', 8)
first_reviewer.rate_hw(bad_student, 'Git', 7)
print(f'bad student: {bad_student.grades}')


# Выставление оценок лекторам
best_student.rate_lector(cool_mentor, 'Python', 10)
best_student.rate_lector(cool_mentor, 'SuperProgrammer', 8)
bad_student.rate_lector(cool_mentor, 'Python', 10)
bad_student.rate_lector(cool_mentor, 'SuperProgrammer', 8)  # Не пройдет оценка - студент не изучает это
print(f'cool_mentor {cool_mentor.grades}')

best_student.rate_lector(any_mentor, 'Python', 10)  # Ошибка - не преподает этот курс
best_student.rate_lector(any_mentor, 'Git', 8)
best_student.rate_lector(any_mentor, 'Basic', 8)
bad_student.rate_lector(any_mentor, 'Git', 10)
bad_student.rate_lector(any_mentor, 'Основы программирования', 8)  # Не пройдет оценка - студент не изучает это
print(f'any_mentor {any_mentor.grades}')


print('\nИнформация об участниках процесса:')

print('\n1.')
print(best_student)
print('\n2.')
print(bad_student)
print('\n3.')
print(cool_mentor)
print('\n4.')
print(any_mentor)
print('\n5.')
print(first_reviewer)
print('\n6.')
print(smart_reviewer)
print()

#------------------
print('Супертест')
persons = [best_student, bad_student, cool_mentor, any_mentor, first_reviewer, smart_reviewer]
for i,pers in enumerate(persons):
    print(f'\n{i+1}.')
    print(pers)
print()
#------------------


#Сравнение средних оценок студентов и преподавателей
print(f'Оценки Джона ниже оценок Васи: {best_student < bad_student}')
print(f'Оценки Джона выше оценок Васи: {best_student > bad_student}')
print(f'Оценки Ивана Петровича ниже оценок Петра Ивановича: {cool_mentor < any_mentor}')
print(f'Оценки Ивана Петровича выше оценок Петра Ивановича: {cool_mentor > any_mentor}')


print()


# Петр Иванович взялся за 'Python' ради получения оценок и проверки функций
any_mentor.add_course('Python')
best_student.rate_lector(any_mentor,'Python', 10)
bad_student.rate_lector(any_mentor,'Python', 9)

print('Средняя оценка по Python у студентов: ',\
    mean_grade_course([best_student, bad_student], 'Python'))
print('Средняя оценка по Python у лекторов:  ',\
    mean_grade_course_mentors([cool_mentor, any_mentor], 'Python'))

