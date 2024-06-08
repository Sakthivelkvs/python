class Cube:
    def __init__(self):
        pass
    def shape(self,l,b,h):
        cube=l * b * h
        print("Volume of Cube:",cube)
class Cylinder:
    def __init__(self):
        pass
    def shape(self,r,he):
        cylinder=3.14*r*he
        print("Volume of Cylinder:",float(cylinder))
class Cuboid:
    def __init__(self):
        pass
    def shape(self,a):
        cuboid=a*a*a
        print("Volume of Cuboid:",cuboid)
obj=Cube()
obj2=Cylinder()
obj3=Cuboid()



while True:
    print("Select an Option")
    print("1.Cube\n2.Cylinder\n3.Cuboid\n4.Exit")
    choice=int(input("Enter Choice"))
    if choice==1:
        lnth=int(input("Enter Length"))
        higth=int(input("Enter Height"))
        width=int(input("Enter Breadth"))
        obj.shape(lnth,higth,width)
        
    elif choice==2:
        r=int(input("Enter Radius"))
        he=int(input("Enter Heigth"))
        obj2.shape(r,he)
        
    elif choice==3:
        a=int(input("Enter Area"))
        obj3.shape(a)
        
    elif choice==4:
        break
    else:
        print("Invalid Choice")
       
