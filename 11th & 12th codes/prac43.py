#Open the file in read mode
file = open("file.txt", "r")

#Read the contents of the file
content = file.read()

#Close the file
file.close()

#Print the contents
print(content)