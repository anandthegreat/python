import datetime

class Employee:
    # These are class variables
    hike_percent = 1.04
    num_employees = 0

    # This is constructor
    def __init__(self,firstname,lastname,pay):
        self.firstname = firstname;
        self.lastname = lastname;
        self.pay = pay;
        self.email = firstname.lower() + lastname.lower()[0] + "@micron.com"
        Employee.num_employees += 1

    # Alternative constructor: provide another way of creating emp from string
    # eg. 'Anand-Verma-125000'
    @classmethod
    def from_string(cls, emp_str):
        firstname,lastname,pay = emp_str.split('-')
        return cls(firstname,lastname,pay)

    def displayName(self):
        print(f"{self.firstname} {self.lastname}")

    def displayEmail(self):
        print(self.email)

    def applyHike(self):
        self.pay = int(self.pay * self.hike_percent)

    @classmethod
    def set_hike_percent(cls,percent):
        cls.hike_percent = percent

    # Does not depend on class or instance variables
    @staticmethod
    def is_weekend(day):
        return day.weekday() == 5 or day.weekday == 6

if __name__ == '__main__':
    s1 = Employee("Anand","Verma",125000)
    s2 = Employee("Anshul","Gautam",110000)

    # Both will give same output
    # s1.displayName();
    # s1.displayEmail();       # instance self is passed automatically
    Employee.displayName(s2);  # We explicitly pass the instance (self)
    Employee.displayEmail(s2);

    # hike_percent now becomes instance variable for s1
    s1.hike_percent = 1.05
    print(Employee.hike_percent)
    print(s1.hike_percent)
    # hike_percent is still a class variable for s2
    print(s2.hike_percent)

    # we can change the class variables and it will reflect in all instances
    Employee.set_hike_percent(1.06)  #Employee class will be passed automatically as the first arg (cls)

    # still 1.05 since hike_percent has become instance variable
    print(s1.hike_percent)
    # 1.06 since it refers to the class variable
    print(s2.hike_percent)

    # Using alternative constructor, the class method for creating instance
    emp_str = 'Rahul-Chaubey-125000'
    s3 = Employee.from_string(emp_str)

    # Using static methods
    todays_date = datetime.date.today()
    print(Employee.is_weekend(todays_date))