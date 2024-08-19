class A:
    def __init__(self):
        print("This is a Init")

    def one(self):
        print("one is working")

    def two(self):
        print("two is working")

class B:
    def __init__(self):
        super().__init__()
        super().two()
        print("THis is B Init")

    def three(self):
        print("Three is Working")

class C(A,B):
    def __init__(self):
        super().__init__() # inherit the medthod and properties of parent class
        print("THis is C Init")

    def four(self):
        print("Four is Working")

b=C()
b.one()