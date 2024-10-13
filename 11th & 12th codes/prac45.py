# To read line by line

file = open("file.txt","r")
a=1  # This is just for numbering of line
line = file.readline()
while line:
    print(a,line)
    line = file.readline()
    a+=1 # to increase the index of line number as we proceed

file.close()