# A code to append data to an already exxisting file.

file_name = "C:\\Users\\Aditya\\Desktop\\aditya.txt"
new_line = "\nThe newly added line at the end of the file."
file = open(file_name,'a')
file.write(new_line)
print("File is appended!")
file.close()