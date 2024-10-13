# os.remove() function is used to delete the file of exsisting file
import os

# Specify the file name to be removed
file_name = "file to be removed.txt"

# Remove/Delete the file
os.remove(file_name)

# file_name variable is created to make accessing it with more ease,
# otherwise directly can put file name ie "file to be removed.txt"
# but some functions do not take input of file name as string
# hence variable declared.