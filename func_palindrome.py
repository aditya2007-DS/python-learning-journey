# A code for checking a palindrome number using function

def is_palindrome(num):
    return str(num) == str(num)[::-1]

n = int(input("Enter a number: "))

if is_palindrome(n):
    print("Palindrome!")
else:
    print("Not Palindrome!")