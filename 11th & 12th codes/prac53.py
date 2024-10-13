# Binary data to write
binary_data = b'\x00\x01\x02\x03\x04\x05' #Bianry data is inputted according to textbk

# Open the binary file in write mode in binary 'wb'
with open ("file.bin","wb") as file:
    # Write the binary data to the file
    file.write(binary_data)

# Close the file (not necessary with the 'with' statement)
#file.close