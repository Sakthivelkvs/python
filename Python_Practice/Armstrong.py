n = int(input("Emter the number "))
len = len(str(n))
print(len)
temp = n
sum = 0
while temp>0:
    r=temp%10          #it returns reminder 
    sum += r**len      #returns sum+reminder*length of a input number
    temp//=10          #it removes the last digits and set the value to next iteration
if n==sum:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")