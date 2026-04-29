# A code to identify a spam comment.

p1 = "Make a lot of money"
p2 = "click this"
p3 = "buy now"
p4 = "subscribe this"

a = input("Enter your comment: ")

if ((p1 in a) or (p2 in a) or (p3 in a) or (p4 in a)):
    print("This comment is a spam!")

else:
    print("This comment is not a spam.")