import students_class
import teachers_class
from monsters_class import *
from monster_workshop import *

# i want to show that i can create a student with first name and last name

student1 = students_class.students('sam', 'jhonson', 1)
student2 = students_class.students('terry', 'berry', 2)
student3 = students_class.students('guyana', 'briggs', 3)

print(student1)
print(student1.f_name, student1.l_name)
print(student2)
print(student2.f_name, student2.l_name)
print(student3)
print(student3.f_name, student3.l_name)

list_student_created = []
list_student_created.append(student1)
list_student_created.append(student2)
list_student_created.append(student3)

for student in list_student_created:
    print(student.f_name, student.l_name)

# do the same for teacher
teacher1 = teachers_class.teacher('filipe', 'paiva', 1)
teacher2 = teachers_class.teacher('james', 'hoddleston', 2)
teacher3 = teachers_class.teacher('angie', 'mcDonald', 3)

list_teacher_created = []
list_teacher_created.append(teacher1)
list_teacher_created.append(teacher2)
list_teacher_created.append(teacher3)

for teacher in list_teacher_created:
    print(teacher.f_name, teacher.l_name)

# do the same for workshops
workshop1 = monster_workshop('Digital scaring:  ', list_teacher_created[0].f_name)
workshop2 = monster_workshop('science of hiding:  ', list_teacher_created[1].f_name)
workshop3 = monster_workshop('history of roaring:  ', list_teacher_created[2].f_name)

list_workshop_created = []
list_workshop_created.append(workshop1)
list_workshop_created.append(workshop2)
list_workshop_created.append(workshop3)

for workshop in list_workshop_created:
    print(workshop.subject, workshop.teacher)

# call method
