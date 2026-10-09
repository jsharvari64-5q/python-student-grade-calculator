
# Student Grade Calculator

# Step 1: Get student details
student_name = input("Enter your name: ")

# Step 2: Get marks for three subjects
marks1 = float(input("Enter marks for Subject 1 (0-100): "))
marks2 = float(input("Enter marks for Subject 2 (0-100): "))
marks3 = float(input("Enter marks for Subject 3 (0-100): "))

# Step 3: Validate marks
if not (0 <= marks1 <= 100):
    print("Invalid marks for Subject 1! Enter marks between 0 and 100.")

elif not (0 <= marks2 <= 100):
    print("Invalid marks for Subject 2! Enter marks between 0 and 100.")

elif not (0 <= marks3 <= 100):
    print("Invalid marks for Subject 3! Enter marks between 0 and 100.")

else:
    # Step 4: Calculate average
    average = (marks1 + marks2 + marks3) / 3

    # Step 5: Assign grade
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

    # Step 6: Display results
    print("\n===== STUDENT REPORT =====")
    print("Name:", student_name)
    print("Subject 1:", marks1)
    print("Subject 2:", marks2)
    print("Subject 3:", marks3)
    print("Average:", round(average, 2))
    print("Final Grade:", grade)
    print("==========================")
