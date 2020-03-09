from monsters_class import *


class teacher(Monster):
    def __init__(self, f_name, l_name, staff_id):
        super().__init__(f_name, l_name)
        self.f_name = f_name
        self.l_name = l_name
        self.staff_id = staff_id

