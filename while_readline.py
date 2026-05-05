# A code to read lines in a file using while loop.

f = open("new_file.txt")

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()