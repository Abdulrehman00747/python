
# STUDENT REPORT CARD SYSTEM


# Step 1: Student Information

student = input("Enter your name: ").strip()
age = int(input("Enter your age: "))
batch = int(input("Enter your batch: "))

print(f"\nWelcome {student}! You are {age} years old and your batch is {batch}.")


# Step 2: String Operations

print("\n------- String Operations -------")

print("Uppercase:", student.upper())
print("Lowercase:", student.lower())
print("Characters:", len(student))
print("Reverse name:", student[::-1])

vowels = 0

for letter in student.lower():
    if letter in "aeiou":
        vowels += 1

print("Number of vowels:", vowels)


# Step 3: Subjects and Marks

print("\n------- Subject Marking -------")

subjects = ["English", "Urdu", "Math", "CS"]
marks = []

for subject in subjects:

    mark = int(input(f"Enter marks for {subject} (0-100): "))

    while mark < 0 or mark > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        mark = int(input(f"Enter marks for {subject}: "))

    marks.append(mark)

print("\nSubjects:", subjects)
print("Marks:", marks)


# Step 4: Calculations

total_marks = sum(marks)
percentage = total_marks / (len(subjects) * 100) * 100
average = total_marks / len(marks)

highest_marks = max(marks)
lowest_marks = min(marks)

print("\n------- Calculations -------")

print("Total marks:", total_marks)
print("Percentage:", percentage, "%")
print("Average:", average)
print("Highest marks:", highest_marks)
print("Lowest marks:", lowest_marks)


# Step 5: Pass / Fail System

passed = percentage >= 50 and lowest_marks >= 50

if percentage >= 50 and lowest_marks >= 50:
    print("Student passed all subjects.")

elif percentage >= 50:
    print("Student passed overall, but failed some subjects.")

else:
    print("Student failed.")


# Grade System 

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\nGrade:", grade)

if passed:
    print("Status: Passed")
else:
    print("Status: Failed")


# Distinction System

if percentage >= 90:
    distinction = "Yes"
else:
    distinction = "No"

print("Distinction:", distinction)


# Step 6: List Operations - Add Subject

print("\n------- Add New Subject -------")

print("Current Subjects:", subjects)
print("Current Marks:", marks)

new_subject = input("\nEnter a new subject to add: ").strip()

new_mark = int(input(f"Enter marks for {new_subject}: "))

while new_mark < 0 or new_mark > 100:
    print("Invalid marks! Enter marks between 0 and 100.")
    new_mark = int(input(f"Enter marks for {new_subject}: "))

subjects.append(new_subject)
marks.append(new_mark)

print("\nAfter Adding:")
print("Subjects:", subjects)
print("Marks:", marks)


# Update Marks

subject_name = input("\nEnter subject name to update marks: ").strip()

if subject_name in subjects:

    index = subjects.index(subject_name)

    updated_mark = int(input("Enter updated marks: "))

    while updated_mark < 0 or updated_mark > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        updated_mark = int(input("Enter updated marks: "))

    marks[index] = updated_mark

    print("Marks updated successfully!")

else:
    print("Subject not found!")


# Step 7: Loops and Marks Above 80

print("\n------- Subject Details -------")

for sub, no in zip(subjects, marks):
    print(f"In {sub}, the student has {no} marks.")

marks_over_80 = 0

for sub, no in zip(subjects, marks):

    if no > 80:
        marks_over_80 += 1
        print(f"{sub} has {no} marks.")

print("Total subjects above 80:", marks_over_80)


# Range Function

print("\nNumbers from 1 to 10:")

for i in range(1, 11):
    print(i)


# Multiplication Table

user_number = int(input("\nEnter a number: "))

for i in range(1, 11):
    print(user_number, "x", i, "=", user_number * i)


# Step 8: Passed and Failed Subjects

passed_sub = []
failed_sub = []

for sub, no in zip(subjects, marks):

    if no >= 50:
        passed_sub.append(sub)
    else:
        failed_sub.append(sub)

print("\nPassed Subjects:", passed_sub)
print("Failed Subjects:", failed_sub)


# Step 9: Final Report Card

# Recalculate after adding/updating marks

total_marks = sum(marks)
percentage = total_marks / (len(subjects) * 100) * 100
average = total_marks / len(marks)

highest_marks = max(marks)
lowest_marks = min(marks)

passed = percentage >= 50 and lowest_marks >= 50

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

distinction = "Yes" if percentage >= 90 else "No"

print("\n")
print(f"{student}'s Report Card".center(55, "-"))

print("\n")
print("SUBJECT:".ljust(22), "MARKS".rjust(12))
print("-" * 35)

for sub, no in zip(subjects, marks):
    print(f"{sub.ljust(22)}:{str(no).rjust(12)}")

print("-" * 35)

print("Total Marks:".ljust(22), str(total_marks).rjust(12))
print("Percentage:".ljust(22), f"{percentage:.2f}%".rjust(12))
print("Average Marks:".ljust(22), f"{average:.2f}".rjust(12))
print("Highest Marks:".ljust(22), str(highest_marks).rjust(12))
print("Lowest Marks:".ljust(22), str(lowest_marks).rjust(12))
print("Grade:".ljust(22), grade.rjust(12))
print("Pass/Fail Status:".ljust(22), ("Pass" if passed else "Fail").rjust(12))
print("Distinction:".ljust(22), distinction.rjust(12))


# Subjects Above 80

above_80_sub = []

for sub, no in zip(subjects, marks):
    if no > 80:
        above_80_sub.append(sub)

print("\nSubjects with above 80 marks:")

for no, sub in enumerate(above_80_sub, start=1):
    print(f"{no}. {sub}")


# Passed Subjects List

print("\nYou are passed in following subjects:")

for no, sub in enumerate(passed_sub, start=1):
    print(f"{no}. {sub}")


# Failed Subjects List

print("\nYou are failed in following subjects:")

for no, sub in enumerate(failed_sub, start=1):
    print(f"{no}. {sub}")


print("\n------- Report Card Completed -------")







