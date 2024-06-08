n =str(input("Enter the Value"))

val = n[::-1]
print(val)

if val == n:
    print("Palindrome")
else:
    print("Not a Palindrome")