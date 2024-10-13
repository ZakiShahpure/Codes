string = input("Enter the STRING to count the characters: ")
sLower = sUpper = sDigit = sSymbol = sSpace = 0
for letter in string:
    if letter.islower():
        sLower+=1
    elif letter.isupper():
        sUpper+=1
    elif letter.isdigit():
        sDigit+=1
    elif letter.isalpha():
        sSymbol+=1
        print(sSymbol)
    elif letter.isspace():
        sSpace+=1

print("The Lower digits are: ",sLower)
print("The Upper digits are: ",sUpper)
print("The total Symbols are: ",sSymbol)
print("The Numerical digits are: ",sDigit)
print("The Spaces are: ",sSpace)