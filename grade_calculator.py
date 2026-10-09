
student_name = input("Enter your name: ")

marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))

print("Welcome,", student_name)
print("Your marks are:", marks1, marks2, marks3)


average = (marks1 + marks2 + marks3) / 3

print("Average marks:", round(average, 2))


if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)


print("\n===== STUDENT REPORT =====")
print("Name:", student_name)
print("Subject 1:", marks1)
print("Subject 2:", marks2)
print("Subject 3:", marks3)
print("Average:", round(average, 2))
print("Final Grade:", grade)
print("==========================")
