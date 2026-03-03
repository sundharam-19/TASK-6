class Employee:
    """Base class for all employees."""
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        """Method to calculate the salary. Should be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement the calculate_salary method")

    def __str__(self):
        """String representation for an employee."""
        return f"{self.name} - {self.__class__.__name__} - Salary: ${self.salary:,.2f}"

class RegularEmployee(Employee):
    """Represents a regular, full-time employee with a fixed annual salary."""
    def __init__(self, name, annual_salary):
        super().__init__(name, annual_salary)
        self.annual_salary = annual_salary

    def calculate_salary(self):
        """Calculates monthly salary by dividing annual salary by 12."""
        self.salary = self.annual_salary / 12
        return self.salary

class ContractEmployee(Employee):
    """Represents a contract employee paid an hourly rate."""
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        """Calculates total salary based on hours worked and hourly rate."""
        self.salary = self.hourly_rate * self.hours_worked
        return self.salary

class Manager(Employee):
    """Represents a manager with a base salary and an annual bonus percentage."""
    def __init__(self, name, base_salary, bonus_percentage):
        super().__init__(name, base_salary)
        self.base_salary = base_salary
        self.bonus_percentage = bonus_percentage

    def calculate_salary(self):
        """Calculates salary including base pay and bonus."""
        bonus_amount = self.base_salary * (self.bonus_percentage / 100)
        self.salary = self.base_salary + bonus_amount
        return self.salary

# Create instances of different employee types
emp1 = RegularEmployee("Alice Smith", 60000)
emp2 = ContractEmployee("Bob Johnson", 50, 160) # $50/hr for 160 hours
emp3 = Manager("Charlie Brown", 80000, 10) # 10% bonus

# Use polymorphism to calculate and display the salary for each employee
employees = [emp1, emp2, emp3]
print("Calculating salaries:")
for employee in employees:
    employee.calculate_salary()
    print(employee)