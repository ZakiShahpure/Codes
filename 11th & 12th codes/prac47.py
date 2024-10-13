# To Read any line in the file

import linecache

file = open("file.txt","r")
d="file.txt"
line = linecache.getline(d,2)

print(line)

file.close()