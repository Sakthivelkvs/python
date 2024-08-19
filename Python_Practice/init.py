# init is used to initialize the variable
# init is like a constructor in java
# the idea behind init is it will automatically call a objects

# the idea behind the self is we are passing self because we are use it

class Computer:
    def __init__(self):         # in this case we did not call this function
        print("This is Init")   # but it will automatically called

    def config(self):
        print("The Config is")

com=Computer()

com.config()




class System:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("The Config is",self.cpu, self.ram)

sys=System("i5","8gb")
sys2=System("Raysen 5","8gb")

sys.config()
sys2.config()
