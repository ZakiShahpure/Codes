#READ THE COMMENTS AS WELL

import time
line = input("Enter a line: ")
lowercount=uppercount=digitcount=alphacount=0
counter=0

print("Lowercase count....")
for a in line :
    if a.islower():
        lowercount+=1
        counter+=1
        time.sleep(1)
        print(counter,"=",a.__str__())  # this change is just to show how to make in output
                                        #position of digit  = digit, is format me ana chahiye isliye dala hai

print("Uppercase count....")
for a in line :
    if a.isupper():                     #|
        uppercount+=1                   #|
        time.sleep(1)                   #|
        counter+=1                      #V
        print(counter)                  #or can do like this for having number of digit in one line and digit in second line
        print(a.__str__())

print("Alphabet count...")      # either pura loop rehne do or, just you can put the
for a in line :                             #print("Alphabet Count is: ", alphacount) if you just want the count
    if a.isalpha():
        alphacount+=1
        time.sleep(1)
        counter+=1
        print(counter)
        print(a.__str__())
    else: print("0")

print("Numeric count....")
for a in line :
    if a.isnumeric():
        digitcount+=1
        time.sleep(1)
        counter+=1
        print(counter)
        print(a.__str__())
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
