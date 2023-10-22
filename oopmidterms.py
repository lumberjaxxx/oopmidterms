class Student:

    def __init__(self, name, student_number, year_level, program):

        self.name = name
        self._student_number = student_number
        self.year_level = year_level
        self.program = program

    def display_student_info(self):
        print(f"Name: {self.name}")
        print(f"Year Level: {self.year_level}")
        print(f"Program: {self.program} \n ") 


class Registrar(Student):

    def __init__(self, name, student_number, year_level, program):
        self.admission_result = False

        Student.__init__(self, name, student_number, year_level, program)

    def Submit_Requirements(self):
        if self.admission_result == True:
            print("Admission result has been received")
        else:
            print("admission result was not recieved") 


    def Registrar_Signed(self):
        if self.admission_result == True:
            print("your admission slip has been signed")
        else:
            print("your admission result wass not been signed")

class Cashier(Student):
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
    def __init__(self,name, student_number, year_level, program):
        self.orgfee = False
        self.csgfee = False
        
        Student.__init__(self,name, student_number, year_level, program)

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
            print( f'{self.name} paid the Org Fee.')
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


class Verify (Cashier):
    def __init__(self, name, year_level, program, status):
        self.verify = True

        Cashier.__init__(self, name, year_level, program, status)

    def verify(self):
        if self.status() == True:
            print(f'{self.name} is cleared ')
        else: 
            print('Please clear your previous requirements')

    def details(self):
        if Cashier.status() == True:
            print(f'{self.name}of {self.year_level} - {self.program} \
                  has complete all the requirement for enrollment.')
            print(f'{self.name} is officially enrolled')


#Student
student1 = Student('Rex', 202280011, "2nd year", "BS Computer Science")
student1.display_student_info()



#Registrar
registrar = Registrar('Rex', 202280011, "2nd year", "BS Computer Science")
registrar.admission_result = True
registrar.Submit_Requirements()
registrar.Registrar_Signed()

#Cashier

# stud1_clearance = Clearance('Rex', 202280011, "2nd year", "BS Computer Science")
# stud1_org = stud1_clearance.verify
# stud1_clearance.Pay_Org()

