n=int(input("Enter a Limit"))
for i in range(2,n+1): # if n=10 it goes until the limit
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag=1
            break
    if flag==1:
        print(i)

# if n = 5
# Outer loop (i from 2 to 5)
    #i = 2:
    #Inner loop: j ranges from 2 to 1 (effectively doesn't run).
    #i=2 j=2 so i%j==0  means 2%2==0
    #flag remains 0.
    #2 is printed (prime)
#i = 3:
    #Inner loop: j ranges from 2 to 2 (effectively doesn't run).
    #i=3 j=2 so i%j==0  means 3%2==1
    #flag remains 0.
    #3 is printed (prime).
#i = 4:
    #Inner loop: j ranges from 2 to 3 (effectively doesn't run).
    #i=4 j=2 so i%j==0  means 4%2==0
    #condition satisfied its break the loop
    #flag remains 1.
    #4 is not printed.
#i = 5:
    #Inner loop: j ranges from 2 to 4 (effectively doesn't run).
    #i=5 j=2 so i%j==0  means 5%2==1
    #i=5 j=3 so i%j==0  means 5%3==1
    #i=5 j=4 so i%j==0  means 5%4==1
    #flag remains 0.
    #5 is printed (prime).






