lst=[1,1,2,3,4,5,5,6,6,7,8,9]
new_lst=[]
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print(new_lst)