# Recursion refers to a funtion call by itself

def factorial(x):
    if x==0:
        return 1

    return x * factorial(x-1)
        
n=int(input("Enter the number "))

result=factorial(n)
print (result)