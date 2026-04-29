# A code of students' result.

marks1 = int(input("Enter marks in Maths: "))
marks2 = int(input("Enter marks in Chemistry: "))
marks3 = int(input("Enter marks in Mechanics: "))
marks4 = int(input("Enter marks in Electronics: "))
marks5 = int(input("Enter marks in Python: "))
marks6 = int(input("Enter marks in Electrical: "))
marks7 = int(input("Enter marks in Physics: "))
marks8 = int(input("Enter marks in Graphics: "))

total_percentage = ((marks1+marks2+marks3+marks4+marks5+marks6+marks7+marks8)/800)*100

print("Total Percentage = ",total_percentage, "%")

if(total_percentage>=40):
    print("Result: Pass!")

elif(total_percentage>100):
    print("Invalid marks!")
else:
    print("Result: Fail!")