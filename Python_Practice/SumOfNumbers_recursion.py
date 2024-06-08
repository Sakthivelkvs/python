def SumOfNumbers(n):
    if n==0:
        return 0        #this condition represents the loop condition when n==0 the iteration will stop here
    
    return n+SumOfNumbers(n-1)  #if n=10 10+9+8+7+6+5+4+3+2+1 so n+recursionfn(n-1)

n=int(input("Enter the number "))

result=SumOfNumbers(n)

print(result)