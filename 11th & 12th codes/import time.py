import time
line = input("Enter a line: ")
lowercount=uppercount=digitcount=alphacount=0
counter=0

for a in line :
    if a.islower():
        lowercount+=1
        time.sleep(1)
        counter+=1
        print(counter,"=",a._str_())  # this change is just to show how to make in output
                                      #position of digit  = digit, is format me ana chahiye isliye dala hai

for a in line :
    if a.isupper():
        uppercount+=1
        counter+=1
        time.sleep(1)
        print(counter,"=",a._str_())

for a in line :
    if a.isalpha():
        alphacount+=1
        time.sleep(1)
        counter+=1
        print(counter)
        print(a._str_())

for a in line :
    if a.isnumeric():
        digitcount+=1
        time.sleep(1)
        counter+=1
        print(counter)
        print(a._str_())
print("Number of lowercase letters: ",lowercount)
print("Number of uppercase letters: ",uppercount)
print("Number of digits are:", digitcount)
print("Number of letters are: ", alphacount)
#input me User dala to output will be               #if space dala to, space will aslo be ignored
#1
#s
#2
#e
#3
#r
#U will be ignored as it is upper case