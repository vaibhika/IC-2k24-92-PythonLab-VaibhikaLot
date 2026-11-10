 
# Student Database using Nested Dictionaries

students = {
    101: {
        "name": "Asha",
        "marks": {"Math": 88, "Physics": 76, "Chem": 92}
    },
    102: {
        "name": "Ravi",
        "marks": {"Math": 35, "Physics": 58, "Chem": 64}
    },
    103: {
        "name": "Meena",
        "marks": {"Math": 72, "Physics": 81, "Chem": 69}
    }
}


# Function to add a student
def add_student():
    roll = int(input("Enter roll number: "))

    if roll in students:
        print("Duplicate roll number! Student already exists.")
        return

    name = input("Enter student name: ")
    marks = {}

    n = int(input("Enter number of subjects: "))

    for i in range(n):
        subject = input("Enter subject name: ")
        score = int(input("Enter marks (0-100): "))

        if score < 0 or score > 100:
            print("Invalid marks! Marks must be between 0 and 100.")
            return

        marks[subject] = score

    students[roll] = {"name": name, "marks": marks}
    print("Student added successfully!")


# Function to update marks
def update_marks():
    roll = int(input("Enter roll number: "))

    if roll not in students:
        print("Student not found!")
        return

    subject = input("Enter subject name: ")
    score = int(input("Enter new marks (0-100): "))

    if score < 0 or score > 100:
        print("Invalid marks! Marks must be between 0 and 100.")
        return

    students[roll]["marks"][subject] = score
    print("Marks updated successfully!")


# Function to delete a student
def delete_student():
    roll = int(input("Enter roll number: "))

    if roll in students:
        del students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found!")


# Function to display student record
def show_student():
    roll = int(input("Enter roll number: "))

    if roll in students:
        print("Roll Number:", roll)
        print("Name:", students[roll]["name"])
        print("Marks:", students[roll]["marks"])
    else:
        print("Student not found!")


# Function to display reports
def reports():

    # Calculate average marks
    averages = {
        roll: round(sum(data["marks"].values()) /
                    len(data["marks"]), 2)
        for roll, data in students.items()
        if data["marks"]
    }

    print("\nStudent Averages:")
    print(averages)

    # Find topper
    if averages:
        topper = max(averages, key=averages.get)
        print("Topper:", students[topper]["name"])

    # Highest scorer in each subject
    print("\nHighest Scorer in Each Subject:")

    subjects = set()

    for data in students.values():
        subjects.update(data["marks"].keys())

    for subject in sorted(subjects):
        scorers = [
            (data["name"], data["marks"][subject])
            for data in students.values()
            if subject in data["marks"]
        ]

        if scorers:
            highest = max(scorers, key=lambda x: x[1])
            print(subject, "->", highest[0], "(", highest[1], ")")

    # Students scoring below 40
    print("\nStudents scoring below 40:")

    below_40 = {
        data["name"]: {
            sub: marks
            for sub, marks in data["marks"].items()
            if marks < 40
        }
        for data in students.values()
        if any(marks < 40 for marks in data["marks"].values())
    }

    print(below_40)

    # Grade-wise grouping
    grades = {"A": [], "B": [], "C": [], "D": [], "F": []}

    for roll, avg in averages.items():

        name = students[roll]["name"]

        if avg >= 90:
            grades["A"].append(name)
        elif avg >= 75:
            grades["B"].append(name)
        elif avg >= 60:
            grades["C"].append(name)
        elif avg >= 40:
            grades["D"].append(name)
        else:
            grades["F"].append(name)

    print("\nGrade-wise Grouping:")
    print(grades)


# Main Menu
while True:

    print("\n===== STUDENT DATABASE MENU =====")
    print("1. Add Student")
    print("2. Update Subject Marks")
    print("3. Delete Student")
    print("4. Show Student Record")
    print("5. Reports")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        update_marks()

    elif choice == 3:
        delete_student()

    elif choice == 4:
        show_student()

    elif choice == 5:
        reports()

    elif choice == 6:
        print("Exiting Student Database. Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")
