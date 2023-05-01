class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.mean_grade} \n'+\
        f'Курсы в процессе изучения: {",".join(self.courses_in_progress)} \nЗавершенные курсы: {",".join(self.finished_courses)}'
        return res
 

    def mean_grade(self):
        '''Средняя оценка за ДР по всем курсам'''
        grades_courses = [sum(x)/len(x) for x in self.grades.values()]  # Список средних оценок по отдельным курсам
        return sum(grades_courses)/len(grades_courses)  # Возвращаем среднюю оценку по всем курсам


    def add_course_progress(self, course_name):
        self.courses_in_progress.append(course_name)   


    def add_course_finished(self, course_name):
        if course_name in self.courses_in_progress:
            self.courses_in_progress.remove(course_name)
        self.finished_courses.append(course_name)   


    def rate_lector(self, lector, course, grade):
        '''Выставление оценки лектору'''
        if course in [self.finished_courses + self.courses_in_progress]:
            if isinstance(lector, Lecturer) and course in lector.courses_attached:
                lector.grades.setdefault(course, [])
                lector.grades[course] += [grade]


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
        # grades_courses = [sum(x)/len(x) for x in list(self.grades.values())] #среднее по каждому курсу
        # grades_mean = sum(grades_courses)/len(grades_courses)
        # res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {grades_mean}'
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.mean_grade()}'
        return res


    def mean_grade(self):
        '''Средняя оценка лектора'''
        # res = 0
        # for x_list in self.grades.values():
        #     res += sum(x_list)/len(x_list)
        # res /= len((self.grades.values()))
        # return res
        grades_courses = [sum(x)/len(x) for x in self.grades.values()]  # Список средних оценок по отдельным курсам
        return sum(grades_courses)/len(grades_courses)  # Возвращаем среднюю оценку по всем курсам


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
            return 'Ошибка'

    def __str__(self):# -> str:
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res









best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
#cool_mentor = Mentor('Some', 'Buddy')
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 10)

 
print(best_student.grades)
print(cool_mentor)

lect1 = Lecturer('Роман','Катин')
lect1.grades = {'abc':[10,2], 'cde':[4,6]}

#grades_all = []
# grades_all = [sum(x)/len(x) for x in list(lect1.grades.values())]
# grades_mean = sum(grades_all)/len(grades_all)

# print(grades_all, grades_mean)
print(lect1)
print(lect1<cool_mentor)