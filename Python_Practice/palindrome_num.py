n = int(input("Enter the Number"))
sum=0
temp = n
while temp>0:
    
    rem=temp%10        # it will return the remider (if n=123 it gives 3)

    sum=sum*10+rem  # now we have to add the reminder to the sum, 
                    # the sum is initalized by 0, if we add the remainder + sum 
                    # if we add sum=sum+rem sum=0+3 sum=3 next iteration it gives 3+2=5 sum=5, so the value is worng 
                    # thats why we need to muliply 10 with the sum so it gives sum=3*10+2 sum=32
                    
    temp=temp//10         # it reset the value of n by dividing by 10,it returns coefficient

print(sum)

if sum==n:
    print("It is an palindrome number")
else:
    print("It is not an palindrome number")

# 1st iteration --> n=123-->rem=123%10 sp               rem=3
                    #sum=0 sum=sum*10+rem sum=0*10+3    sum=3
                    #n=123//10                          n=12 -->final sum=3
                                                    


                    #now n=12 it will start the value with 12 on next iteration when(12>0)

# 2nd iteration --> rem=12%10 rem=2
                    #sum=3*10+2 sum=32
                    #n=12//10 n=1 -->final sum=32

                    #now n=1 it will start the value with 12 on next iteration when(1>0)

# 2nd iteration --> #rem=1%10 rem=1
                    #sum=32*10+1 sum=321
                    #n=1//10 n=0

                    #now n=0 it will check the condition when(0>0)
                    # it will exit the loop


                    #if we want to check the palindrome are not, just assign the value of n is to another tempravory variable
                    # and check temp==n
                 