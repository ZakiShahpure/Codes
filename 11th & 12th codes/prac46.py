# To insert an additional line in the exsisting file.txt 

file = open("file.txt","a")
file.write("\n This is an additional line") #\n is for entering this line on a new
                                            #line in the existing file
file.close()