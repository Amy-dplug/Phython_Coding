#Get Student score from user
score = int(input("Enter the student's score (0-100): "))
#Determine the grade basd on the score
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

#Display the grade
print(F"the student's grade is {grade}")