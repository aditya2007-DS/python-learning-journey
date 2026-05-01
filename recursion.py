# A code recursive code of summing first 'n' numbers.

def sum(n):
    if (n==1):
        return 1
    return sum(n-1) + n

n = int(input("Enter the first numbers whose sum is to be calculated: "))

print(f"The sum is: {sum(n-1) + n}")