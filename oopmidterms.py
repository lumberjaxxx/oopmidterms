class Student:

    def __init__(self, name, student_number, year_level, program):

        self.name = name
        self.year_level = year_level
        self.program = program

    def display_student_info(self):
        print(f"Name: {self.name}")
        print(f"year_level: {self.year_level}")
        print(f"program: {self.program}")


class Registrar:
    pass

class Cashier(Studet):
    def __init__(self):
        self.balance= False
        self.pay= False

    def Check_Balance(self):
        if self.balance ==True:
            print(f'Have balance.')
        else:
            print(f'No Balance')
        
    def Pay_Balance(self):
        if self.pay==True:
            print(f'Balance already paid.')
        else:
            print(f'Please pay your balance.')
            


class Clearance(Student):
    def __init__(self,name,year_level,program):
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

    def Pay_Org(self):
        if self.orgfee==True:
            print(f'Already cleared in Org Fee.')
            print( f'{Student.name} paid the Org Fee.')
        elif self.csgfee==True:
            print(f'Already cleared in CSG Fee.')
        else:
            print(f'Is not cleared.')

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




student1 = Student("Spledelyn Cristine Recarze",202280045,"2nd Year","BS Computer Science")
student1.display_student_info()
stud1_registrar = Registrar()
stud1_clearance = Clearance()
stud1_clearance.Pay_Org(True)
