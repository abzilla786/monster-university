# from pip._vendor.distlib.compat import raw_input
# from students_class import *
# from teachers_class import *
# from workshop import *
# import stdiomask
# from monsters_class import *
# from monster_workshop import *
#
#
# class Login:
#
#     # logins_created = [{
#     #     'id': 'admin',
#     #     'password': 'admin'
#     # }
#     def __init__(self, id, password):
#         self.id = id
#         self.password = password
#         self.error = "Enter a valid username and password"
#
#     # call method that verifies input vs the class variables
#     # see how to access class variables
#     def check(self):
#         loop = True
#         while loop:
#             list_of_students = []
#             list_of_teachers = []
#             list_workshop_created = []
#             skills = []
#
#             if (self.id == log_id and self.password == log_pass):
#                 print("Login successful")
#
#                 def print_menu():  ## Your menu design here
#                     print(30 * "-", "MENU", 30 * "-")
#                     print("1. Create student")
#                     print("2. Create Teacher")
#                     print("3. Create Workshop")
#                     print("4. Add Skills for students")
#                     print("5. View Student list")
#                     print("6. View Teachers list")
#                     print("7. View Workshop list")
#                     print("8. Exit")
#                     print(67 * "-")
#
#                 loop = True
#
#                 while loop:  # While loop which will keep going until loop = False
#                     print_menu()  # Displays menu
#                     choice = int(input("Enter your choice [1-7]: "))
#
#                     if choice == 1:
#                         print("Create student has been selected")
#                         student_id = 0
#                         user_input = " "
#
#                         while user_input != 'quit':
#                             student_id += 1
#                             firstname = input('Please enter the first name: ')
#                             lastname = input('Please enter the last name: ')
#                             student = students(firstname, lastname, student_id)
#                             list_of_students.append(student)
#                             user_input = input('Would you like to add another student? y/n ')
#                             if user_input == 'n':
#                                 user_input = 'quit'
#                             else:
#                                 pass
#                     elif choice == 2:
#                         print("Create teacher has been selected")
#                         teacher_id = 0
#                         user_input = " "
#
#                         while user_input != 'quit':
#                             teacher_id += 1
#                             firstname = input('Please enter the first name: ')
#                             lastname = input('Please enter the last name: ')
#                             teachers = teacher(firstname, lastname, teacher_id)
#                             list_of_teachers.append(teachers)
#                             user_input = input('Would you like to add another teacher? y/n ')
#                             if user_input == 'n':
#                                 user_input = 'quit'
#                             else:
#                                 pass
#                     elif choice == 3:
#                         print("Create workshop has been selected")
#                         user_input = " "
#                         while user_input != 'quit':
#                             workshop_name = input('Please enter the first name: ')
#                             teacher_name = input('Please enter the last name: ')
#                             number_of_attendees = int(input('please enter number of attendees for subject: '))
#                             workshop = Workshops_available(workshop_name, teacher_name, number_of_attendees)
#                             list_workshop_created.append(workshop)
#                             user_input = input('Would you like to add another workshop? y/n ')
#                             if user_input == 'n':
#                                 user_input = 'quit'
#                             else:
#                                 pass
#                     elif choice == 4:
#                         print("Add skills to students has been selected")
#                         user_input = ' '
#                         while user_input != 'quit':
#                             print("New skills for students.")
#                             for ppl in list_of_students:
#                                 print(ppl.f_name, ppl.l_name, ppl.student_id)
#                             chosen_student_id = input("Enter student ID to add skills to: ")
#                             int_chosen_id = int(chosen_student_id)
#                             chosen_student = list_of_students[int_chosen_id - 1]
#                             add_skill = input("Add an appropriate skill: ")
#                             chosen_student.skills.append(add_skill)
#                             print(chosen_student.skills)
#                             user_input = input("Would you like to add more skills? y/n ")
#                             if user_input == 'n':
#                                 user_input = "quit"
#                             else:
#                                 pass
#
#                     elif choice == 5:
#                         print("View students has been selected")
#                         user_input = " "
#                         while user_input != 'quit':
#                             i = 0
#                             for i in range(len(list_of_students)):
#                                 print(f"student: {list_of_students[i].f_name} {list_of_students[i].l_name} "
#                                       f"{list_of_students[i].student_id} {list_of_students[i].skills}")
#                             print('number of students in list: ' + str(len(list_of_students)))
#                             user_input = input('Please enter quit to go back to the main menu: ')
#                     elif choice == 6:
#                         print("View teachers has been selected")
#                         user_input = " "
#                         while user_input != 'quit':
#                             i = 0
#                             for i in range(len(list_of_teachers)):
#                                 print(f"student: {list_of_teachers[i].f_name} {list_of_teachers[i].l_name} "
#                                       f"{list_of_teachers[i].staff_id}")
#                             print('number of teachers in list: ' + str(len(list_of_teachers)))
#                             user_input = input('Please enter quit to go back to the main menu: ')
#                     elif choice == 7:
#                         print("View workshops has been selected")
#                         user_input = " "
#                         while user_input != 'quit':
#                             i = 0
#                             for i in range(len(list_workshop_created)):
#                                 print(f"student: {list_workshop_created[i].subject} {list_workshop_created[i].teacher} "
#                                       f"{list_workshop_created[i].list_of_attendees}")
#                             print('number of Workshops available: ' + str(len(list_workshop_created)))
#                             user_input = input('Please enter quit to go back to the main menu: ')
#                     elif choice == 8:
#                         print("Goodbye")
#                         # You can add your code or functions here
#                         loop = False  # This will make the while loop to end as not value of loop is set to False
#                     else:
#                         # Any integer inputs other than values 1-7 we print an error message
#                         raw_input("Wrong option selection. Enter any key to try again..")
#             elif (self.id != log_id and self.password != log_pass):
#                 print(self.error)
#                 try_again = input('Would you like to try again (Y/N): ')
#                 if try_again == 'N':
#                     print('Goodbye')
#                     loop = False
#                 else:
#                     pass
#             continue
#
#
# log = Login("admin", "admin")
# log_id = input("Enter your user ID: ")
# log_pass = stdiomask.getpass("Enter password: ")
# log.check()
