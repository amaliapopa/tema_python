class Employee:
    """Common base class for all employees"""
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.emp_count += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.emp_count}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.emp_countp -=1


    def update_salary(self, new_salary):
        self.salary = new_salary

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager(Employee):
    mgr_count = 0
    
    def __init__(self, name, salary, department):
        nume_echipa = "F27"
        super().__init__(name, salary)
        self.department = f"{nume_echipa}_{department}"
        Manager.mgr_count += 1

    # POPA - 4 litere -> x % 3 = 1 -> afiseaza doar salariul angajatului
    def display_employee(self):
        print("Salary: ", self.salary)

    def __del__ (self):
        Manager.mgr_count -=1

if __name__ == "__main__":
    # AMALIAIOANA - 11 litere -> y/3=3 -> 3 obiecte apartinand clasei Manager
    mgr1 = Manager("Stefan", 9000, "IT")
    mgr2 = Manager("Ion", 3000, "Cashier")
    mgr3 = Manager("Vasilica", 6200, "Secretary")

    mgr1.display_employee()
    mgr2.display_employee()
    mgr3.display_employee()

    print(f"Number of managers: {Manager.mgr_count}")
    print(f"Number of employees: {Employee.emp_count}")

    

