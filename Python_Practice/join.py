# Python join() is an inbuilt string function used to join elements of a sequence separated by a string separator.

str1="Hello"
val="_".join(str1)
print(val)

# OP: H_e_l_l_o

list1=['s','a','k','t','h','i']
print(list1)
var=''.join(list1)
var2='*'.join(list1)
var3=" ".join(list1)
print("1.",var," ","2.",var2," ","3.",var3)

# OP: ['s', 'a', 'k', 't', 'h', 'i']
#     1. sakthi   2. s*a*k*t*h*i   3. s a k t h i