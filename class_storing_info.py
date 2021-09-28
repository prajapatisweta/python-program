# 28/9
# 7 a

class student:
    def __init__(self, sno, sname, age, course):
        self.sno=sno
        self.sname=sname
        self.age= age
        self.course = course
    def displayStudentDetails(self):
        print("*******Student Details are******** ")
        print("Student No. ", self.sno)
        print("Student Name ", self.sname)
        print("Student Age ", self.age)
        print("Student Course ", self.course)
print("Enter Details for student 1: ")
sn1=int(input("Enter No. :- "))
name1=input("Enter Name :- ")
age1=sn=int(input("Enter Age :- "))
course1=input("Enter Course :- ")

s1=student(sn1, name1, age1, course1)

print("Enter Details for student 2: ")
sn2=int(input("Enter No. :- "))
name2=input("Enter Name :- ")
age2=int(input("Enter Age :- "))
course2=input("Enter Course :- ")

s2=student(sn2, name2, age2, course2)

print("Enter Details for student 3: ")
sn3=int(input("Enter No. :- "))
name3=input("Enter Name :- ")
age3=int(input("Enter Age :- "))
course3=input("Enter Course :- ")

s3=student(sn3, name3, age3, course3)

s1.displayStudentDetails()
s2.displayStudentDetails()
s3.displayStudentDetails()