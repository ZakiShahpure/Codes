year= int(input("enter year"))
all = year % 4 == 0 and (year % 100 !=0 or year % 400==0)
if all:
    print ("its a leap year")

else:
    print ("not a leap year")
