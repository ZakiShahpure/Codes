#Check if a string contains only alphabetical characters:

string = "Dream"                    # Can also take input from user
print("Default inputted string is: ", string)
stringinput = input("Enter a string (without spaces) to check for alphabetical characters")

print(string.isalpha())
print(stringinput.isalpha())
