# A code to understand the write mode in file.

str = "Aditya has a huge interest in Data Analysis."

f = open("my_file.txt","w")
f.write(str)
f.close()