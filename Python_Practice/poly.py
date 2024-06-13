class Cube:
    def __init__(self, l, b, h):
        self.l = l
        self.b = b
        self.h = h

    def volume(self):
        return self.l * self.b * self.h

class Cylinder:
    def __init__(self, r, he):
        self.r = r
        self.he = he

    def volume(self):
        return 3.14 * self.r * self.r * self.he

class Cuboid:
    def __init__(self, a):
        self.a = a

    def volume(self):
        return self.a * self.a * self.a

def main():
    while True:
        print("Select an Option")
        print("1. Cube\n2. Cylinder\n3. Cuboid\n4. Exit")
        choice = int(input("Enter Choice: "))
        
        if choice == 1:
            lnth = int(input("Enter Length: "))
            b = int(input("Enter Breadth: "))
            h = int(input("Enter Height: "))
            shape = Cube(lnth, b, h)
            print("Volume of Cube:", shape.volume())
        elif choice == 2:
            r = int(input("Enter Radius: "))
            he = int(input("Enter Height: "))
            shape = Cylinder(r, he)
            print("Volume of Cylinder:", shape.volume())
        elif choice == 3:
            a = int(input("Enter Side Length: "))
            shape = Cuboid(a)
            print("Volume of Cuboid:", shape.volume())
        elif choice == 4:
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
