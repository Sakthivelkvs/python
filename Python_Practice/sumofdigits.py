def SUmofDigits(value):
    sum=0
    while value>0:
        rem=value%10
        sum=sum+rem
        value=value//10
    print(sum)

value=int(input("Enter the number"))

SUmofDigits(value)
