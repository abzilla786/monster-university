from monster_workshop import *


class Workshops_available(Monster_workshop):
    def __init__(self, subject, teacher, list_of_attendees):
        super().__init__(self, subject, teacher)
        self.subject = subject
        self.teacher = teacher
        self.list_of_attendees = list_of_attendees
