class Student:
    
    def __init__ (self, name, year_level, program):
        pass

class Registrar:
    pass

class Cashier:
    pass

class Clearance():
    def __init__(self, name, year_level, program):
        self.name = name
        self._student_number = student_number
        self.yearlevel = year_level
        self.program = program
        self.OrgFee = False
        self.CsgFee = False
        self.status = True

    def get(self):
        return (self._student_number)

    def PayOrg(self):
        if {self.OrgFee}== True:
            return f'{self.name} paid the Org Fee.'

    def CSGFee(self):
        if {self.CsgFee} == True:
            return f'{self.CsgFee} paid the CSG Fee.'

    def signing(self):
        if {self.status}==False:
            return f'The clearance of {self.name} with a student number of {self._student_number}///' \
                   f' and a {self.year_level} from the program of {self.program} is already signed. '


class Verification(Student, Cashier):

    def __init__(self, name, year_level, program, status):
        self.verify = True

        Student.__init__(self, name, program, year_level)
        Cashier.__init__(self, status)

    def verify(self):
        if Cashier.status() == True:
            print(f'{Student.name} is cleared ')
        else: 
            print('Please clear your previous requirements')

    def details(self):
        if Cashier.status() == True:
            print(f'{Student.name}of {Student.year_level} - {Student.program} \
                  has complete all the requirement for enrollment.')
            print(f'{Student.name} is officially enrolled')




student1 = Clearance("Spledelyn Cristine Recarze",202280045,"2nd Year","BS Computer Science")
