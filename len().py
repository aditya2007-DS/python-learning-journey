# acode to find length of a string without len()

text = input("Enter a text: ")

count = 0

for _ in text:
    count += 1

print("Length = ",count)