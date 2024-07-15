arr=[1,2,3,4,5]
leng=len(arr)
n=int(input("Enter the number of you want to search in array:"))
flag =False
for i in range(0,leng):
    if n==arr[i]:
        flag=True
        break
if flag==False:
    print("Number not found")
else:
    print("Number Found")

