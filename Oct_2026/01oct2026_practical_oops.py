# ============================================================
# OOP PRACTICE — BANK ACCOUNT
# ============================================================
#
# Create a BankAccount class that represents a customer's
# bank account.
#
# Your goal is to practice:
# - Classes
# - Objects
# - __init__()
# - self
# - Attributes
# - Methods
# - Changing object state
# - Returning values
# - Basic validation
class BankAccount():
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
        else:
            print('This is an invalid amount')
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance = self.balance - amount
            else:
                print('Account does not have sufficient balance')
        else:
            print('Amount can not be 0')
    def check_balance(self):
        print(f'Dear {self.account_holder} you current balance is:\n{self.balance}')
    def display_account(self):
        print(f'Account Holder Name: {self.account_holder}\nAccount Number: {self.account_number}\nTotal Balance: {self.balance}')
account = BankAccount("Ali", "12345", 1000)
#print(account.balance)
#deposit_function = account.deposit(-12)
#account.withdraw(1500)
#account.check_balance()
account.display_account()
#print(account.balance)

'''✅ Bank Account OOP — Successfully created a BankAccount class with attributes, initialization, deposit, withdrawal, balance checking, and account display methods.

🧠 Demonstrated understanding of classes, objects, self, attributes, methods, and changing object state through methods.

🔧 Key improvements: Allow withdrawal of the entire balance by using <= instead of <, print the invalid withdrawal message, and return the balance from check_balance() when the value needs to be used by the caller.

🏆 Score: 9.0/10 | OOP Practice — IN PROGRESS'''



# ------------------------------------------------------------
# REQUIREMENT 1 — CREATE THE CLASS
# ------------------------------------------------------------
#
# Create a class called BankAccount.
#
# The class should have these attributes:
#
#   account_holder
#   account_number
#   balance
#
# These values should be received through __init__().       
# ------------------------------------------------------------
# REQUIREMENT 2 — DEPOSIT
# ------------------------------------------------------------
#
# Create a method:
#
#   deposit(amount)
#
# Rules:
#
# - The amount must be greater than 0.
# - If the amount is valid, add it to the balance.
# - If the amount is 0 or negative, reject the deposit.
#
#
# ------------------------------------------------------------
# REQUIREMENT 3 — WITHDRAW
# ------------------------------------------------------------
#
# Create a method:
#
#   withdraw(amount)
#
# Rules:
#
# - The amount must be greater than 0.
# - The customer cannot withdraw more money than the
#   current balance.
# - If the withdrawal is valid, subtract it from the balance.
# - Otherwise, reject the withdrawal.
#
#
# ------------------------------------------------------------
# REQUIREMENT 4 — CHECK BALANCE
# ------------------------------------------------------------
#
# Create a method:
#
#   check_balance()
#
# It should return the current balance.
#
#
# ------------------------------------------------------------
# REQUIREMENT 5 — DISPLAY ACCOUNT
# ------------------------------------------------------------
#
# Create a method:
#
#   display_account()
#
# It should display:
#
# Account Holder: <name>
# Account Number: <number>
# Balance: <balance>



# ============================================================
# OOP PRACTICE — EMPLOYEE MANAGEMENT
# ============================================================
#
# Create an Employee class that represents an employee
# in a company.
#
# Practice:
# - Class
# - Object
# - __init__()
# - self
# - Attributes
# - Methods
# - Changing object state
# - Returning values
# - Basic validation
#
#
# ------------------------------------------------------------
# REQUIREMENT 1 — CREATE THE CLASS
# ------------------------------------------------------------
#
# Create a class called Employee.
class Employee():
    def __init__(self,name,id,department,salary):
        self.name =name
        self.id = id
        self.department = department
        self.salary = salary
    def display_employee(self):
        print(f'Employee Name: {self.name}\nEmployee ID: {self.id}\nDepartment: {self.department}\nSalary: {self.salary}')
    def increase_salary(self, amount):
        if amount > 0:
            self.salary = self.salary + amount
        else:
            print('amount is invalid, so increment is not possible')

    def change_department(self, new_department):
        self.department = new_department
    def get_annual_salary(self):
        annual_salary = self.salary * 12
        print(f'Hello {self.name}, Your annual salary is: {annual_salary}')
employee = Employee("Ali","EMP001","Data Science",3000)
#print(employee.display_employee())
#print(employee.increase_salary(-500))
#print(employee.salary)
#employee.increase_salary(500)
#print(employee.salary)

#✅ Employee OOP — Successfully created an Employee class with initialization, attributes, display functionality, salary modification, department modification, and annual salary calculation.

#🧠 Demonstrated strong understanding of classes, objects, self, attributes, methods, and modifying object state through methods. Successfully transferred the OOP concepts from the BankAccount exercise to a new domain.

#🔧 Key learning: get_annual_salary() should return the calculated value rather than only printing it. Also, methods that already print should normally be called directly rather than wrapped in print().

#🏆 Score: 9.5/10 | OOP Practice — IN PROGRESS



# The employee should have these attributes:
#
#   name
#   employee_id
#   department
#   salary
#
# These values should be provided when creating the object.
#
#
# ------------------------------------------------------------
# REQUIREMENT 2 — DISPLAY EMPLOYEE
# ------------------------------------------------------------
#
# Create a method:
#
#   display_employee()
#
# It should display:
#
# Employee Name: <name>
# Employee ID: <employee_id>
# Department: <department>
# Salary: <salary>
#
#
# ------------------------------------------------------------
# REQUIREMENT 3 — INCREASE SALARY
# ------------------------------------------------------------
#
# Create a method:
#
#   increase_salary(amount)
#
# Rules:
#
# - amount must be greater than 0.
# - If valid, increase the employee's salary by that amount.
# - If amount is 0 or negative, reject the increase.
#
#
# ------------------------------------------------------------
# REQUIREMENT 4 — CHANGE DEPARTMENT
# ------------------------------------------------------------
#
# Create a method:
#
#   change_department(new_department)
#
# The method should update the employee's department.
#
#
# ------------------------------------------------------------
# REQUIREMENT 5 — GET ANNUAL SALARY
# ------------------------------------------------------------
#
# Create a method:
#
#   get_annual_salary()
#
# The employee's salary is monthly.
#
# Return the employee's annual salary.
#
#
# ------------------------------------------------------------
# REQUIREMENT 6 — TEST YOUR CLASS
# ------------------------------------------------------------
#
# Create this employee:
#
# employee = Employee(
#     "Ali",
#     "EMP001",
#     "Data Science",
#     3000
# )
#
# Then:
#
# 1. Display the employee information.
# 2. Increase the salary by 500.
# 3. Change the department to "AI Engineering".
# 4. Get the annual salary.
# 5. Display the updated employee information.
#
#
# ------------------------------------------------------------
# EXPECTED RESULTS
# ------------------------------------------------------------
#
# Initial monthly salary:
# 3000
#
# After salary increase:
# 3500
#
# Annual salary:
# 42000
#
# Final department:
# AI Engineering


