# To read only one line (here only first line)
# The only diff is there is no loop

file = open("file.txt", "r")

#Read the contents of the file
line = file.readline()

#Print the contents
print(line)

#Close the file
file.close()