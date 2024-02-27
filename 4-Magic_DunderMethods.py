'''
Magic or Dunder methods start and end with '__'
Allow operator overloading and other functionalities
eg. __init__,__str__,__len__,__add__,__mul__,__or__
'''

class Employee:

    hike_percent = 1.04

    def __init__(self,firstname,lastname,pay):
        self.firstname = firstname;
        self.lastname = lastname;
        self.pay = pay;
        self.email = firstname.lower() + lastname.lower()[0] + "@micron.com"

    def displayName(self):
        print(f"{self.firstname} {self.lastname}")

    def applyHike(self):
        self.pay = int(self.pay * self.hike_percent)

    # repr is meant to be unambigous, shows a way to re-create the object
    # meant for debugging by developers
    # if __str__ is not defined, __repr__ will be used
    def __repr__(self):
        return f'Employee({self.firstname},{self.lastname},{self.pay})'

    # str is meant to be readable
    def __str__(self):
        return f'{self.firstname} {self.lastname}, {self.email}'

    # to overload '+' operator
    def __add__(self, other):
        return self.pay + other.pay

    # overload the len() method
    def __len__(self):
        return len(self.firstname + self.lastname)

if __name__ == '__main__':
    e1 = Employee('Hanuman','Ji Maharaj',108000)
    e2 = Employee('Angad', 'Ji', 80000)
    print(e1.__repr__())
    print(repr(e1))
    print(Employee.__repr__(e1))

    print(str(e1))
    print(e1+e2)  # invoke __add__ dunder
    print(Employee.__add__(e1,e2))

    print(len(e1))
