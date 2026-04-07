# A code for generating the table of 2.

num = int(input("Enter a number who's table is to be generated: "))

for i in range(1, 11):
    print(num,"x",i,"=", num*i)
