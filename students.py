
class Student:
	def __init__(self, name, surname, gender):
		self.name = name
		self.surname = surname
		self.gender = gender
		self.finished_courses = []

stud1 = Student('Вася', 'Иванов', 'М')
stud1.finished_courses += ['Algebra']

new_course = 'Zhopakurs'
stud1.finished_courses.append(new_course)

print(stud1.finished_courses)



# ============================================================

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python']
best_student.grades['Git'] = [10, 10, 10, 10, 10]
best_student.grades['Python'] = [10, 10]
 
print(best_student.finished_courses)
print(best_student.courses_in_progress)
print(best_student.grades)
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
print(cool_mentor.courses_attached)