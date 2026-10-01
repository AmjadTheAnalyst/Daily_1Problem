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

#Problem 03
# ============================================================
# OOP PRACTICE — PRODUCT
# ============================================================
#
# Create a Product class that represents a product in an
# online store.
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
# Create a class called Product.
class Product():
    def __initi__(self, name, id, price, stock):
        self.name = name
        self.id = id
        self.price = price
        self.stock = stock
    def display_product(self):
        print(f'Product Name: {self.name}\nID: {self.id}\nPrice: {self.price}\nStock: {self.stock}')

    def add_stock(self,quantity):
        if quantity > 0:
            self.stock = self.stock + quantity
        else:
            print('Please enter the correct quantity')
    def sell(self,quantity):
        if quantity > 0:
            if self.stock >= quantity:
                self.stock = self.stock - quantity
            else: 
                print('Stock is insufficient')
    def get_total_value(self):
        value = (self.stock * self.price)
        return value
product = Product("Laptop","P001",1000,10)

#✅ Product OOP — Successfully created a Product class with product attributes, display functionality, stock addition, selling logic, and total stock value calculation.

#🧠 Demonstrated strong understanding of object state and correctly used return in get_total_value(). The main issue was the sell() comparison: quantity == stock only allows selling the entire inventory. The condition should allow any valid quantity up to the available stock.

#🔧 Key learning: Use <= when the boundary value is also valid, and handle invalid quantities explicitly.

#🏆 Score: 8.5/10 | OOP Practice — IN PROGRESS

# Create a method:
#
#   get_total_value()
#
# Return the total value of the current stock.
#
# Formula:
#
#   price × stock
#
# Example:
#
# price = 50
# stock = 10
#
# total value = 500



# The product should have these attributes:
#
#   name
#   product_id
#   price
#   stock
#
# These values should be provided when creating the object.
#
#
# ------------------------------------------------------------
# REQUIREMENT 2 — DISPLAY PRODUCT
# ------------------------------------------------------------
#
# Create a method:
#
#   display_product()
#
# It should display:
#
# Product Name: <name>
# Product ID: <product_id>
# Price: <price>
# Stock: <stock>
#
#
# ------------------------------------------------------------
# REQUIREMENT 3 — ADD STOCK
# ------------------------------------------------------------
#
# Create a method:
#
#   add_stock(quantity)
#
# Rules:
#
# - quantity must be greater than 0.
# - If valid, increase the stock by that quantity.
# - Otherwise, print an appropriate message.
#
#
# ------------------------------------------------------------
# REQUIREMENT 4 — SELL PRODUCT
# ------------------------------------------------------------
#
# Create a method:
#
#   sell(quantity)
#
# Rules:
#
# - quantity must be greater than 0.
# - The customer cannot buy more than the available stock.
# - If valid, decrease the stock by that quantity.
# - Otherwise, print an appropriate message.
#
#
# ------------------------------------------------------------
# REQUIREMENT 5 — GET TOTAL VALUE
# ------------------------------------------------------------
#
# Create a method:
#
#   get_total_value()
#
# Return the total value of the current stock.
#
# Formula:
#
#   price × stock
#
# Example:
#
# price = 50
# stock = 10
#
# total value = 500
#
#
# ------------------------------------------------------------
# REQUIREMENT 6 — TEST YOUR CLASS
# ------------------------------------------------------------
#
# Create this product:
#
# product = Product(
#     "Laptop",
#     "P001",
#     1000,
#     10
# )
#--------------------------------------------------------------------------------------------------------
#Problem 04
# OOP Challenge — Order

# Create an Order class with:
# 1. customer_name
# 2. order_id
# 3. items (a list of dictionaries)
class Order():
    def __init__(self, name, id, items ): # items {"name": "Laptop", "price": 1000, "quantity": 2}
        self.name = name
        self.id = id
        self.items = items

    def display_order(self):
        print(f'Product Name: {self.name}\nID: {self.id}\nAll Items: {self.items}')
    def add_item(self, name, price, quantity):
        if price > 0 and quantity > 0:
            new_item = {'name': name, 'price': price, 'quantity': quantity}
            self.items.append(new_item)
    def calculate_total(self):
        total_quantity = []
        for value in range(0,len(self.items)):
            item_price = (self.items[value]['price']) * (self.items[value]['quantity'])  
            total_quantity.append(item_price)    
        return sum(total_quantity) 
    def get_item_count(self):
        #total_items = self.items[0]['quantity'] 
        #return total_items
        total_quantity = 0
        for value in range(0,len(self.items)):
            total_quantity = total_quantity + self.items[value]['quantity']
        return total_quantity

order = Order("Ali", "ORD001", [])
order.add_item("Laptop", 1000, 2)
order.add_item("Mouse", 50, 3)
order.add_item("Keyboard", 80, 1)

order.display_order()

total = order.calculate_total()
print("Total:", total)

count = order.get_item_count()
print("Item Count:", count)

#✅ Order OOP — Successfully created an Order class that stores customer information and a collection of order items.

#🧠 Demonstrated strong understanding of object state, lists of dictionaries, method-based state modification, validation, iteration, calculation, and returning values from methods.

#💡 Successfully introduced the concept of an object containing and working with multiple items through self.items.

#🔧 Minor improvements: display_order() should label self.name as Customer Name rather than Product Name, and direct iteration over self.items can simplify the loops.


#🏆 Score: 9.7/10 | OOP Practice — IN PROGRESS

# 4. get_item_count()
#    RETURN the total number of items ordered.



#    Print the customer name, order ID, and all ordered items.

# Each item will look like:
# {"name": "Laptop", "price": 1000, "quantity": 2}

# Methods:

# 1. display_order()
#    Print the customer name, order ID, and all ordered items.

# 2. add_item(name, price, quantity)
#    Add a new item to the order.
#    Quantity must be greater than 0.
#    Price must be greater than 0.

# 3. calculate_total()
#    Calculate and RETURN the total order price.
#    Formula:
#    price × quantity for each item

# 4. get_item_count()
#    RETURN the total number of items ordered.
#    Example:
#    Laptop quantity 2 + Mouse quantity 3 = 5


# Test your class:

order = Order("Ali", "ORD001", [])

order.add_item("Laptop", 1000, 2)
order.add_item("Mouse", 50, 3)
order.add_item("Keyboard", 80, 1)

order.display_order()

total = order.calculate_total()
print("Total:", total)

count = order.get_item_count()
print("Item Count:", count)


# Expected:
# Total: 2230
# Item Count: 6

a = [{"name": "Laptop", "price": 1000, "quantity": 2}]
#i want to know the total price of laptop for total quantity
price = a[0]['price'] * a[0]['quantity']
print(price)