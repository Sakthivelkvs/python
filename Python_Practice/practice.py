# # Check Armstronng Number

def check_Armstrog(n):
    l=len(str(n))
    temp=n
    sum=0
    while temp>0:
        rem=temp%10
        sum=sum+rem**l
        temp=temp//10
    if n==sum:
        print("Its a Armstrong")
    else:
        print("its not")

num=int(input("enter the Number: "))
check_Armstrog(num)


# Print Armstromg Number Upto Limit

def Armstrong_limit(strt,end):
    strt=100
    for i in range(strt, end+1):
        size=len(str(i))

        sum=0
        temp=i

        while temp>0:
            rem=temp%10
            sum=sum+rem**size
            temp=temp//10
        if i==sum:
            print(i,end=" ")
            print()
    
s=int(input("enter the Starting: "))
e=int(input("Enter the limit: "))
Armstrong_limit(s,e)  


# print prime number upto limit

def prime_number(num):
    for i in range(2, num+1):
        prime = False
        for j in range(2, i):
            if i%j==0:
                prime = True
                break
        if prime==False:
            print(i)

n=int(input("enter the Number: "))
prime_number(n)



# Check prime or not

def check_prime(num):

    for i in range(2, num):
        if n%i==0:
            print("its not Prime")
            break
    else:
        print("its a prime")
n=int(input("enter the Number: "))
check_prime(n)


# find a duplicate in an list

def duplicates_list():
    lst=["Sakthi","vel","Akash","Mohan","Akash","MK","Sakthi"]
    lst_size=len(lst)

    for i in range(0, lst_size):
        for j in range(i+1, lst_size):
            if lst[i]==lst[j]:
                print(len(lst[i]))

duplicates_list()


# find a factorial of a number

def find_factorial(num):
    fact=1
    for i in range(1, num+1):
        fact=fact*i
    print(fact)

n=int(input("enter the Number: "))
find_factorial(n)



# find a factorial of a number using recursion

def factorial(n):
    if n==0:
        return 1
    return n* factorial(n-1)

num=int(input("enter the Number: "))
res=factorial(num)
print(res)

# find sum of numbers

def sumOfNum(num):
    sum=0
    for i in range(1, num+1):
        sum=sum+i
    print(sum)


num=int(input("enter the Number: "))
sumOfNum(num)


# find a sum of a number using recursion

def SumOfNumber(n):
    if n==0:
        return 0
    return n+SumOfNumber(n-1)

num=int(input("enter the Number: "))
res=SumOfNumber(num)
print(res)

#find sum of Digits of a given number

def sumOfDig(num):
    sum=0
    number=str(num)
    for i in number:
        sum=sum+int(i)
    print(sum)
n=int(input("enter the Number: "))
sumOfDig(n)

def SumOfDigs(num):
    sum=0
    while num>0:
        rem=num%10
        sum=sum+rem
        num=num//10
    print(sum)
n=int(input("enter the Number: "))
SumOfDigs(n)  



#find sum of Digits of a given number using recursion

def SumOfDigits(n):
    if n==0:
        return 0
    
    return n%10 + SumOfDigits(n//10)

num=int(input("enter the Number: "))
res=SumOfDigits(num)
print(res)


# Print all fibonacci Series

def fibonacci(num):
    s=1
    e=0
    if n==0:
        print(e)
    elif n==1:
        print(s)
    else:
        for i in range(2,num):
            fib=s+e
            s=e
            e=fib
            print(fib,end=" ")
        print()

n=int(input("enter the Number: "))
res=fibonacci(n)
print(res)


# Print fibonacci Series using recursion:

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

num=int(input("enter the Number: "))
for i in range(num):
    print(fib(i),end=" ")
print()


# print sum of even numbers:

def sumOfEven(num):
    sum=0
    for i in range(1,num+1):
        if i%2==0:
            sum=sum+i
    print(sum)

n=int(input("enter the Number: "))
sumOfEven(n)


# reverses a string and counts the number of characters in the reversed string:

def revrse(s):
    rev=s[::-1]

    space=rev.replace(" ", "")
    count=len(space)

    print("the reversed stirng is: ",rev,"the count of the revesed string is: ",count)

n=str(input("enter the String: "))
revrse(n)

#          
# #        
# # #      
# # # #    
# # # # #

def patt1(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print()

num=int(input("enter the Number: "))
patt1(num)

# # # # #
# # # #
# # #
# #
#

def patt2(n):
    for i in range(n):
        for j in range(i,n):
            print("*",end=" ")
        print()

num=int(input("enter the Number: "))
patt2(num)

        #
      # #
    # # #
  # # # #
# # # # #


def patt3(n):
    for i in range(n):
        for j in range(i,n):
            print(" ",end=" ")
        for j in range(i+1):
            print("#",end=' ')
        print()

num=int(input("enter the Number: "))
patt3(num)

# # # # #
  # # # #
    # # #
      # # 
        #

def patt6(n):
    for i in range(n):
        for j in range(i+1):
            print(" ",end=" ")
        for j in range(i,n):
            print("#",end=' ')
        print()

num=int(input("enter the Number: "))
patt6(num)


     #
    # #
   # # #
  # # # #
 # # # # #

def patt4(n):
    for i in range(n):
        for j in range(i,n):
            print("",end=" ")
        for j in range(i+1):
            print("#",end=' ')
        print()

num=int(input("enter the Number: "))
patt4(num)

