# A code to calculate table of a number using function.

def print_table(num):
    for i in range (1,11):
        print(num, "X", i, "=", num*i)

n = int(input("Enter a number: "))
print_table(n)