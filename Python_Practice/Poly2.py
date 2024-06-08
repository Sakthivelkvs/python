class Volume:
    def shape(self, type, l=0, b=0, h=0, r=0, he=0, a=0):
        if type == "Cube":
            cube = l * b * h
            print("Volume of Cube:", cube)
        elif type == "Cylinder":
            cylinder = 3.14 * r * r * he
            print("Volume of Cylinder:", cylinder)
        elif type == "Cuboid":
            cuboid = a * a * a
            print("Volume of Cuboid:", cuboid)

def main():
    obj = Volume()

    while True:
        print("Select an Option")
        print("1. Cube\n2. Cylinder\n3. Cuboid\n4. Exit")
        choice = int(input("Enter Choice: "))
        
        if choice == 1:
            lnth = int(input("Enter Length: "))
            b = int(input("Enter Breadth: "))
            h = int(input("Enter Height: "))
            obj.shape("Cube", l=lnth, b=b, h=h)
        elif choice == 2:
            r = int(input("Enter Radius: "))
            he = int(input("Enter Height: "))
            obj.shape("Cylinder", r=r, he=he)
        elif choice == 3:
            a = int(input("Enter Side Length: "))
            obj.shape("Cuboid", a=a)
        elif choice == 4:
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
