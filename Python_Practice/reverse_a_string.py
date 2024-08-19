# str1 = "Sakthi is a Bright"
# str2 =""
# for i in str1:
#     str2=i + str2           # in each iteration the current character is added to beggining of str2

# print("Original: ",str1)
# print("reversed: ",str2)



def reverse(str1):
    rev_str=""
    for i in str1:
        rev_str=i + rev_str
    print("Reversed String: ",rev_str)

s = str(input("Enter the string: "))

reverse(s)


# Iteration 1:
# i = 'S'
# str2 = 'S' + "" -> str2 = "S"

# Iteration 2:
# i = 'a'
# str2 = 'a' + "S" -> str2 = "aS"

# Iteration 3:
# i = 'k'
# str2 = 'k' + "aS" -> str2 = "kaS"


def reverse_string(str1):
    return str1[::-1]


s = input("Enter the string: ")
reversed_s = reverse_string(s)
print("Reversed string:", reversed_s)




#_______________________________________####__________________________________________________________________#

# Question
# input : I am Sakthi
# outPut: i ht kaSmaI



