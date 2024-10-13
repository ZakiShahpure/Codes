""" if file = open "Student.txt","a" dala to overwrite nahi hamesha run karne pe 
    new data exsisting ke sath likha jayega, old data wont be deleted.
    if we write "r" in place of a then everytime we run the code, check by running
    the code.
"""
print("===============Student Record===============")
count = int(input("Number of records to enter:   "))
file = open ("Student.txt","a")

for i in range(count):
    print("Enter Details of Student", (i+1), "Below: ")
    name = input("Name     :")
    rolln = int(input("Roll Number     :"))
    rec = name +","+ str(rolln)+"\n"
    file.write(rec)
    file.flush()
file.close