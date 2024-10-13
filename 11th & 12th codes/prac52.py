import linecache

# Open the file in read mode
file = open("file1.txt","r")
file_name = "file1.txt"

line = linecache.getline(file_name, 2) #format is (filename, line number)


print(line)

# Close the file
file.close()

# Alternate code
import linecache
import time

# Open the file in read mode
file = open("file1.txt","r")
file_name = "file1.txt"         
a=1                             # in this line 3 dala as us file me 3 lines hai,
while a <=3 :                   # warna loop hatake bhi kar sakte hai
    time.sleep(1)               # one by one karna hai to dusra code already present.
    line = linecache.getline(file_name, a) #format is (filename, line number)
    print(line)
    a+=1

# Close the file
file.close()