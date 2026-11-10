
# Employee Database using Dictionaries

employees = {
    "E1": {"name": "Kiran", "dept": "IT", "salary": 60000},
    "E2": {"name": "Sara", "dept": "HR", "salary": 45000},
    "E3": {"name": "Dev", "dept": "IT", "salary": 75000},
    "E4": {"name": "Nina", "dept": "Finance", "salary": 52000},
    "E5": {"name": "Omar", "dept": "HR", "salary": 48000}
}


# 1. Add Employee
def add_employee():
    emp_id = input("Enter employee ID: ")

    if emp_id in employees:
        print("Employee ID already exists!")
        return

    name = input("Enter employee name: ")
    dept = input("Enter department: ")
    salary = float(input("Enter salary: "))

    employees[emp_id] = {
        "name": name,
        "dept": dept,
        "salary": salary
    }

    print("Employee added successfully!")


# 2. Update Employee Salary
def update_salary():
    emp_id = input("Enter employee ID: ")

    if emp_id in employees:
        salary = float(input("Enter new salary: "))
        employees[emp_id]["salary"] = salary
        print("Salary updated successfully!")
    else:
        print("Employee not found!")


# 3. Delete Employee
def delete_employee():
    emp_id = input("Enter employee ID: ")

    if emp_id in employees:
        del employees[emp_id]
        print("Employee deleted successfully!")
    else:
        print("Employee not found!")


# 4. Search Employee by ID
def search_employee():
    emp_id = input("Enter employee ID: ")

    if emp_id in employees:
        print("Employee ID:", emp_id)
        print("Name:", employees[emp_id]["name"])
        print("Department:", employees[emp_id]["dept"])
        print("Salary:", employees[emp_id]["salary"])
    else:
        print("Employee not found!")


# 5. Reports
def reports():

    # Department-wise payroll and headcount
    payroll = {}
    headcount = {}

    for emp in employees.values():
        dept = emp["dept"]

        payroll[dept] = payroll.get(dept, 0) + emp["salary"]
        headcount[dept] = headcount.get(dept, 0) + 1

    print("\nDepartment-wise Payroll and Headcount:")

    for dept in payroll:
        print(dept, "Payroll:", payroll[dept],
              "Headcount:", headcount[dept])


    # Highest-paid employee in each department
    highest_paid = {}

    for emp_id, emp in employees.items():
        dept = emp["dept"]

        if dept not in highest_paid:
            highest_paid[dept] = (emp["name"], emp["salary"])

        elif emp["salary"] > highest_paid[dept][1]:
            highest_paid[dept] = (emp["name"], emp["salary"])

    print("\nHighest Paid Employee in Each Department:")

    for dept, details in highest_paid.items():
        print(dept, "->", details[0], "(", details[1], ")")


    # Employees sorted by salary (highest first)
    sorted_employees = sorted(
        employees.items(),
        key=lambda x: x[1]["salary"],
        reverse=True
    )

    print("\nEmployees Sorted by Salary:")

    for emp_id, emp in sorted_employees:
        print(emp_id, emp["name"], emp["salary"])


    # Give 10% raise to employees earning below 50000
    # A new dictionary is created so that the original
    # employee records remain unchanged.

    new_employees = {
        emp_id: {
            "name": emp["name"],
            "dept": emp["dept"],
            "salary": emp["salary"] * 1.10
        }
        if emp["salary"] < 50000
        else emp.copy()

        for emp_id, emp in employees.items()
    }

    print("\nNew Dictionary After 10% Raise:")

    for emp_id, emp in new_employees.items():
        if employees[emp_id]["salary"] < 50000:
            print(emp["name"], "->", emp["salary"])

    print("\nOriginal Salaries (Unchanged):")

    for emp_id, emp in employees.items():
        if emp["salary"] < 50000:
            print(emp["name"], "->", emp["salary"])


    # Department with highest average salary
    total_salary = {}
    count = {}

    for emp in employees.values():
        dept = emp["dept"]

        total_salary[dept] = total_salary.get(dept, 0) + emp["salary"]
        count[dept] = count.get(dept, 0) + 1

    average_salary = {
        dept: total_salary[dept] / count[dept]
        for dept in total_salary
    }

    print("\nDepartment-wise Average Salary:")
    print(average_salary)

    if average_salary:
        highest_dept = max(average_salary, key=average_salary.get)
        print("Department with Highest Average Salary:",
              highest_dept, average_salary[highest_dept])


# Main Menu
while True:

    print("\n===== EMPLOYEE DATABASE MENU =====")
    print("1. Add Employee")
    print("2. Update Salary")
    print("3. Delete Employee")
    print("4. Search Employee by ID")
    print("5. Reports")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_employee()

    elif choice == 2:
        update_salary()

    elif choice == 3:
        delete_employee()

    elif choice == 4:
        search_employee()

    elif choice == 5:
        reports()

    elif choice == 6:
        print("Exiting Employee Database. Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")
