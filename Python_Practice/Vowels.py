# Count Vowels in a String_______________________________________________________________________________________________________________________

def CountVowels(w):
    vow="aeiou"
    low=w.lower()
    count=0
    for char in low:        # irerate  each vowel is in the input string
        if char in vow:   # checks each input string in vow variable
            count=count+1
    print(count)

wrd=str(input("Enter a Word: "))
CountVowels(wrd)

#Check if a String Contains All Vowels_______________________________________________________________________________________________________________________


def StringContainsAllVowels(w):
    vow = "aeiou"
    low = w.lower()  # Convert the input string to lowercase to handle case insensitivity

    # Check if each vowel is in the input string
    for char in vow:
        if char not in low:
            return False  # Return False if any vowel is missing
    
    return True  # Return True if all vowels are found

# Example usage
wrd = input("Enter a Word: ")
result = StringContainsAllVowels(wrd)
print(result)  # Output will be True or False


# ___________another Method_________________


def StringContainsAllVowels(w):
    vow="aeiou"
    low = w.lower()

    a_letter=e_letter=i_letter=o_letter=u_letter=False

    for char in low:
        if char in "a":
            a_letter=True
        elif char in "e":
            e_letter=True
        elif char in "i":
            i_letter=True
        elif char in "o":
            o_letter=True
        elif char in "u":
            u_letter=True
    
    if a_letter and e_letter and i_letter and o_letter and u_letter:
        print("Accepted")
    else:
        print("Not Accepted")


wrd = input("Enter a Word: ")
StringContainsAllVowels(wrd)



# Replace Vowels in a String_______________________________________________________________________________________________________________________

def replace_string(w,rplce):
    vow="aeiou"
    res=''
    low=w.lower()

    for char in low:
        if char in vow:
            res=res+rplce
        else:
            res=res+char
    print(res)

wrd = input("Enter a Word: ")
replace=input("Enter a Replacement Word: ")
replace_string(wrd,replace)


# Find the posion of the vowel_______________________________________________________________________________________________________________________

def findPosition(s):
    vowels="aeiou"
    low=s.lower()
    pos=[]
    index=0
    for i in low:
        if i in vowels:
            pos.append(index)
        index=index+1
    print("the position of the vowel is: ",pos)
    # return pos
wrd = input("Enter a Word: ")
findPosition(wrd)

#Remove the Vowels from a string_______________________________________________________________________________________________________________________

def removeVowels(s):
    vow="aeiou"
    low=s.lower()
    res=""
    for i in low:
        if i not in vow:
            res=res+i
    print(res)

wrd = input("Enter a Word: ")
removeVowels(wrd)


