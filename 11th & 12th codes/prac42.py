#Specifying the file path
file_path = './file.txt'

#Open the file in write mode
with open (file_path, "w") as file:
                    # w stands for write mode
    file.write('Life is one time opportunity !\n')
    file.write("There is rewind button no validity")

#File creation is successful/complete
print (f'File "{file_path}" created successfully')