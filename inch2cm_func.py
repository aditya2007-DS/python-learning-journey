# A code to convert inches to cms using function.

def inch_to_cm(inch):
    return inch*2.54

inch = int(input("Enter the value in inches: "))

print(f"The corresponding value in cms is: {inch_to_cm(inch)}")