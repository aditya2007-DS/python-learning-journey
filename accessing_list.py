# A program for accessing an element from a list.

l = [10, 20, 30, 40, 50]

index = int(input("Enter the index you want to access: "))

i = 0

while i < len(l):
    if i == index:
        print("Element at index", index, "=", l[i])
        break
    i += 1
else:
    print("Invalid index!")