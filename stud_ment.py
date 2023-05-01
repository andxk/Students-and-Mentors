class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_course(self, course_name):
        self.finished_courses.append(course_name)   
 
     
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

    def rate_lector(self, lector, course, grade):
        '''Выставление оценки лектору'''
        if isinstance(lector, Lecturer) and course in self.courses_attached:
            self.grades.setdefault(course, [])
            self.grades[course] += [grade]

    


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










best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)