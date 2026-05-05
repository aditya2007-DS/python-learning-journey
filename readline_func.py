# A code to read multiple lines in a file.
# The output is a list.

f = open("new_file.txt")
lines = f.readlines()
print(lines, type(lines))
f.close()