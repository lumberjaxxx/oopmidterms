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

class Clearance():
    def __init__(self,Name,StudentNumber,YearLevel,Program):
        self.name = Name
        self._studentnumber = StudentNumber
        self.yearlevel = YearLevel
        self.program = Program
        self.OrgFee = False
        self.CsgFee = False
        self.status = True

    def get(self):
        return (self._studentnumber)

    def PayOrg(self):
        if {self.OrgFee}== True:
            return f'{self.name} paid the Org Fee.'

    def CSGFee(self):
        if {self.CsgFee} == True:
            return f'{self.CsgFee} paid the CSG Fee.'

    def signing(self):
        if {self.status}==False:
            return f'The clearance of {self.name} with a student number of {self._studentnumber}///' \
                   f' and a {self.yearlevel} from the program of {self.program} is already signed. '

student1 = clearance("Spledelyn Cristine Recarze",202280045,"2nd Year","BS Computer Science")


print(student1.name)
print(student1.yearlevel)
print(student1.program)
print(student1.OrgFee)
print(student1.CsgFee)
print(student1.status)










class Encoder(Student):

    Student.__init__(name, student_number, year_level, program)

    def checkClearance(self):
        pass

    def encodeCourses(self):
        pass

    def prospectus(self):
        pass
