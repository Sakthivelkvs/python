def square_of_num(lst):
    new_lst=[]
    for i in lst:
        new_lst.append(i*i)
    return new_lst


f_list=[1,2,3,4,5,6]
f_out=square_of_num(f_list)
print(f_out)