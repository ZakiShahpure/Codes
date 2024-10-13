# Open the file in read mode
file = open ("file.txt","r")

# Read the contents of the file
content = file.read()

# Split the contents of the file in the list tof substrings
substrings = content.split()

#Close the file
file.close()

# Print the substring

for substring in substrings:
    print(substring)