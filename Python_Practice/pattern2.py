#####
#####
#####
#####
#####  #Print the Pattren i*j


n=5
for i in range(n):              #i_represents_rows
    for j in range(n):          #j_represents_Column
        print("*",end=" ")      #end_remains_same_line
    print()                     #to_break_line

    

#          #i=0,j++,out=*
# #        #i=1,j++,out=**
# # #      #i=1,j++,out=***
# # # #    #i=1,j++,out=****
# # # # #  #i=1,j++,out=*****

#Print_the_Pattern_increassing_order


n=5
i=1
for i in range(n):
    for j in range(1,i+2):
        print(j,end=" ")
    print()

# # # # #
# # # #
# # #
# #
#Print_pattern_Decreasing _order

n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


        #
      # #
    # # #
  # # # #
# # # # #Print_the_Pattern_The_pattern_have_both_increasing_and_decreasing_order_increasing_have_Space_and_decresing_have_#

n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(" ", end=" ")
    for j in range(1,i+2):
        print(j, end=" ")
    print()


# # # # #
  # # # #
    # # #
      # # 
        #Print_the_Pattern_Inseasing_have_Space_and_Decreasing_have_#

n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("@",end=" ")
    print()




        #
      # # #
    # # # # #
  # # # # # # #
# # # # # # # # #


#Print_the_Pattren

n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):      #removes_one_column
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()


#
# #
# # #
# # # #
# # # # #
# # # #
# # #
# #
#

#Print this Pattern

n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i,n):
        print(" ",end=" ")
    print()
for i in range(n-1):
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i+1):
        print(" ",end=" ")
    print()


# # # # # # # # #
  # # # # # # #
    # # # # #
      # # #
        #

#Print_the_pattern

n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()







