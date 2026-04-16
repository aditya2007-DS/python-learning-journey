# A code to check whether a password is strong or not

password = input("Enter password: ")

if len(password) >= 8:
    print("Strong Password!!!")
else:
    print("Weak Password :(")