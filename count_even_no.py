# A code to count even numbers in list

nums = [1, 4, 7, 10, 13, 16]
count = 0

for n in nums:
    if n % 2 == 0:
        count += 1

print("Even numbers:", count)