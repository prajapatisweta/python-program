# 7 b  28/9
class CompanyMember:
    def __init__(self, name, designation, age):
        self.name= name
        self.designation= designation
        self.age = age
    def tell(self):
        print(" Name:- ", self.name, "\n Designation:- ", self.designation, \
            "\n Age:- ", self.age)

class FactoryStaff(CompanyMember):
    def __init__(self, name, designation, age, overtime_allow):
        CompanyMember.__init__(self,name, designation, age,)
        self.overtime_allow = overtime_allow
    def displayFactoryStaff(self):
        print("\n Factory Staff Details: ")
        CompanyMember.tell(self)
        print(" OverTime Allowance:- ", self.overtime_allow)

class OfficeStaff(CompanyMember):
    def __init__(self, name, designation, age, travel_allow):
        CompanyMember.__init__(self,name, designation, age,)
        self.travel_allow = travel_allow
    def displayOfficeStaff(self):
        print("\n Office Staff Details: ")
        CompanyMember.tell(self)
        print(" Travel Allowance:- ", self.travel_allow)

f1= FactoryStaff("Ana", "Senior Engineer", 35, 1500)
f2= FactoryStaff("James", "Assistant Engineer", 26, 1700)
o1= OfficeStaff("Sam", "HR admin", 45, 1400)

# f1.tell()
f1.displayFactoryStaff()
f2.displayFactoryStaff()
o1.displayOfficeStaff()
