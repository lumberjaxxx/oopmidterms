class Student:
    
    def __init__ (self, name, student_number, year_level, program):
        pass

class Registrar:
    pass

class Cashier:
    pass


class Clearance(Student):
    def __init__(self):
        self.orgfee = False
        self.csgfee = False
        
        Student.__init__(self,name,year_level,program)

    def Pay_Org(self):
        if self.orgfee==True:
            print(f'Already cleared in Org Fee.')
        elif self.csgfee==True:
            print(f'Already cleared in CSG Fee.')
        else:
            print(f'Is not cleared.')

class Encoder(Student):

    Student.__init__(name, student_number, year_level, program)

    def checkClearance(self):
        pass

    def encodeCourses(self):
        pass

    def prospectus(self):
        pass
