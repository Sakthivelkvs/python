class Student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def show(self):
        print(self.name,self.rollno)

    class Laptop:
        def __init__(self,ram,pro):
            self.ram=ram
            self.pro=pro

        def show(self):
            print(self.ram,self.pro)

name=str(input("Enter Name"))
roll=int(input("Enter Roll Number"))
ram=int(input("Enter Ram"))
processor=str(input("Enter Processor"))


s1=Student(name,roll)
l1=Student.Laptop(ram,processor)

s1.show()
l1.show()



