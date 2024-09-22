# Find All Divisors of a Number______________________________________________________________________________________________________________________


def factorize(n):
    divisor=[]
    for i in range(1, n+1):
        if n % i== 0:
            divisor.append(i)
    print(divisor)
num=int(input("enter the Number: "))
factorize(num)


# Check if a Number is Prime (using divisors)______________________________________________________________________________________________________________________


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1): # n ** 0.5 gives the square root of n.
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
if is_prime(n):
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")

# Sum of Divisors of a Number________________________________________________________________________________________________________________________________

def sumOfDivisors(n):
    sum=0
    div=[]
    for i in range(1,n+1):
        if n%i==0:
            sum=sum+i
            div.append(i)
    print("the divisors are:",div)
    print("the sum of all divisors are:",sum)
num=int(input("enter the Number: "))
sumOfDivisors(num)



#  Find the Greatest Common Divisor (GCD)______________________________________________________________________________________________________________________


def gcd(n1,n2):
    div1=[]
    div2=[]
    for i in range(1,n1+1):
        if n1%i==0:
            div1.append(i)
    print("the Divisor of First Number is",div1)
    for j in range(1,n2+1):
        if n2%j==0:
            div2.append(j)
    print("the Divisor of Second Number is",div2)

    fnl_gcd=[]
    for p in div1:
        for q in div2:
            if p==q:
                fnl_gcd.append(q)

    result=max(fnl_gcd)
    print("the GCD Is: ",result)


num1=int(input("enter the 1st Number: "))
num2=int(input("enter the 2nd Number: "))
gcd(num1,num2)

# Another Way to Find GCD______________________________________________________________________________________________________________________

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("GCD of", a, "and", b, "is:", gcd(a, b))

# Find the Number of Divisors______________________________________________________________________________________________________________________________

def nofdivisors(n):
    tot=0
    div=[]
    for i in range(1,n+1):
        if n%i==0:
            div.append(i)
            tot=tot+1
    print("the divisors are: ",div)
    print("the Number of Divisors are: ",tot)

num=int(input("enter the Number: "))
nofdivisors(num)

#Check if a Number is a Perfect Number__________________________________________________________________________________________________________________

def perfectNumber(n):
    sum=0
    div=[]
    for i in range(1,n):
        if n%i==0:
            div.append(i)
            sum=sum+i
    print("the divisors are: ",div)       
    print("the Sum of Divisors: ",sum)
    if sum==n:
        print("the",n,"is a Perfect Number")
    else:
        print("Its not the Perfect Number")

num=int(input("enter the Number: "))
perfectNumber(num)


#Find All Numbers with a Given Number of Divisors_______________________________________________________________________________________________________________________


# If d = 4 and the range is from 1 to 10, you need to find all numbers between 1 and 10 that have exactly 4 divisors.
# Example 1:
# Let’s say you need to find numbers with exactly 4 divisors in the range from 1 to 20.

# Number 6: Divisors are 1, 2, 3, 6 → 4 divisors
# Number 8: Divisors are 1, 2, 4, 8 → 4 divisors
# Number 10: Divisors are 1, 2, 5, 10 → 4 divisors
# Number 15: Divisors are 1, 3, 5, 15 → 4 divisors
# Thus, the numbers with exactly 4 divisors in the range 1 to 20 are 6, 8, 10, 15.

# Example 2:
# If d = 3 and the range is from 1 to 10:

# Number 4: Divisors are 1, 2, 4 → 3 divisors
# So, the only number with exactly 3 divisors in the range 1 to 10 is 4.


def FindallDivisors(lim,div):
    res=[]
  
    for num in range(1,lim+1):
        divisor=[]
        count=0
        for j in range(1, num+1):
            if num%j==0:
                count=count+1
                divisor.append(j)
        print(j,".",divisor)
        if count==div:
            res.append(j)
    print("All Numbers with a Given Number of Divisors is: ",res)

l=int(input("enter the Limit: "))
d=int(input("enter the No.of divisiors: "))
FindallDivisors(l,d)

#Print the divisors in descending order_______________________________________________________________________________________________________________________

def divisorSort(n):
    div=[]
    for i in range(1,n+1):
        if n%i==0:
            div.append(i)
    div.sort(reverse=True)
    print(div)


l=int(input("enter the Limit: "))

divisorSort(l)



  