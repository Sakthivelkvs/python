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
