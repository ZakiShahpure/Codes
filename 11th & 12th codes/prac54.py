byte_list = [100, 56, 35, 94]
byte_array = bytes(byte_list)

try:
    with open("bytes_array.txt", "wb") as f:
        f.write(byte_array)
        print(str(byte_array) + "Successfully Stored in File....")

except Exception as e:
    print(e)