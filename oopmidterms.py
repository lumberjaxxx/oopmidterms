class Student:

    def __init__(self, name, student_number, year_level, program):
        self.name = name
        self._student_number = student_number
        self.year_level = year_level
        self.program = program


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
