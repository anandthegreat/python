class Employee:
    # These are class variables
    hike_percent = 1.04

    # This is constructor
    def __init__(self,firstname,lastname,pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = firstname.lower() + lastname.lower()[0] + "@micron.com"

    def displayName(self):
        print(f"{self.firstname} {self.lastname}")

    def applyHike(self):
        self.pay = int(self.pay * self.hike_percent)


class Developer(Employee):

    hike_percent = 1.10

    def __init__(self,firstname,lastname,pay,coding_lang):
        super().__init__(firstname,lastname,pay)
        self.coding_lang = coding_lang

class Manager(Employee):

    def __init__(self,firstname,lastname,pay,employees=None):
        super().__init__(firstname,lastname,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def show_emps(self):
        for emp in self.employees:
            emp.displayName()

if __name__ == '__main__':

    d1 = Developer('Anand','Verma',125000,'Python')
    d2 = Developer('Rahul','Chaubey',126000,'JavaScript')

    m1 = Manager('Srikanth','Chillapalli',150000,[d1,d2])

    m1.show_emps()

    print(isinstance(d1,Developer)) #True
    print(isinstance(d1,Employee))  #True
    print(isinstance(m1,Developer)) #False

    print(issubclass(Manager,Employee))  #True
    print(issubclass(Developer,Manager)) #False