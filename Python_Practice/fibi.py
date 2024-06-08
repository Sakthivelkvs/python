def fibi(n):
    s=1
    f=0
    if n==0:
        print(f)
    elif n==1:
        print(s)
    else:
        for i in range(2,n):
            t=s+f
            s=f
            f=t
            print(t)
n=int(input("Enter the Number"))
res=fibi(n)