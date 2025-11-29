class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_bonus(self):
        return self.salary * 0.10

    def get_annual_salary(self):
        return self.salary

    def get_total_salary(self):
        return self.salary + self.get_bonus()

class Manager(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name, salary)

    def get_bonus(self):
        return self.salary * 0.20

    def get_long_term_bonus(self):
        return self.salary * 0.50

def main():
    emp = Employee("John", "Doe", 50000)
    print(f"Employee: {emp.first_name} {emp.last_name}, Annual Salary: ${emp.get_annual_salary()}, Bonus: ${emp.get_bonus()}")

    mgr = Manager("Jane", "Smith", 80000)
    print(f"Manager: {mgr.first_name} {mgr.last_name}, Annual Salary: ${mgr.get_annual_salary()}, Bonus: ${mgr.get_bonus()}, Long Term Bonus: ${mgr.get_long_term_bonus()}")

main()
