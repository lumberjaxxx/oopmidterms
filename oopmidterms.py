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
            print("Admission result has been received ")
        else:
            print("admission result was not recieved") 


    def Registrar_Signed(self):
        if self.admission_result == True:
            print("your admission slip has been signed \n ")
        else:
            print("your admission result was not been signed \n ")

class Cashier(Student):
    def __init__(self,name, student_number, year_level, program):
        self.balance= False
        self.pay= True

        Student.__init__(self,name, student_number, year_level, program)

    def Check_Balance(self):
        if self.balance ==True:
            print(f'{self.name} has balance.')
            self.pay = False
        else:
            print(f'{self.name} has no remaining balance')
            return self.pay
        
    def Pay_Balance(self):
        if self.pay==True:
            print(f'Balance has been cleared. \n')
        else:
            print('Transaction declined')
            print(f'Please pay your balance. \n')

            

class Clearance(Student):
    def __init__(self,name, student_number, year_level, program):
        self.orgfee = False
        self.csgfee = False
        self._status = False
        
        Student.__init__(self,name, student_number, year_level, program)

    def get_status(self):
        pass

    def Pay_Org(self):
        if self.orgfee==True:
            print(f'Already cleared in Org Fee.')
            print( f'{self.name} paid the Org Fee.')
        else:
            print(f'Is not cleared.')
            print('Please proceed to clearing your Org fee.')

    def CSGFee(self):
        if self.csgfee == True:
            print(f'{self.name} paid the CSG Fee.')
        else:
            print(f'Is not cleared.')
            print('Please proceed to clearing your CSG fee.')

    def signing(self):
        if self._status==True:
            print(f'The clearance of {self.name} with a student number of {self._student_number} \nand a {self.year_level} from the program of {self.program} is already signed. \n ')
        else:
            print('Transaction not completed. Try Again.')


class Verify (Clearance):
    def __init__(self, name, student_number, year_level, program):
        Clearance.__init__(self, name, student_number, year_level, program)
        

    def get_status(self):
        self._status = True   
    
    def verify(self):
        if self._status == True:
            print(f'{self.name} is cleared ')
        else: 
            print('Please clear your previous requirements')

    def details(self):
        if self._status == True:
            print(f'{self.name} of {self.year_level} - {self.program} has complete all the requirement for enrollment.')
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
cashier = Cashier('Rex', 202280011, "2nd year", "BS Computer Science")
cashier.balance = False
cashier.Check_Balance()
cashier.Pay_Balance()

#Clearance

clearance = Clearance('Rex', 202280011, "2nd year", "BS Computer Science")
clearance.orgfee = True
clearance.csgfee = True
stat = clearance._status = clearance.orgfee and clearance.csgfee
clearance.Pay_Org()
clearance.CSGFee()
clearance.signing()

#Verification
verify = Verify('Rex', 202280011, "2nd year", "BS Computer Science")
verify.get_status()
verify.verify()
verify.details()
