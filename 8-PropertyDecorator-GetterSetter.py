class Employee:
    def __init__(self,firstname: str, lastname:str):
        self.firstname = firstname
        self.lastname = lastname

    # Getter: Using property decorator we can access email just like an attribute
    @property
    def email(self):
        if self.firstname and self.lastname:
            return f"{self.firstname.lower()}.{self.lastname.lower()}@google.com"
        return "Unable to create email id"

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.firstname = first
        self.lastname = last

    @fullname.deleter
    def fullname(self):
        self.firstname = None
        self.lastname = None

if __name__ == '__main__':
    e1 = Employee('Anand','Verma')
    print(e1.email)

    print(e1.fullname)
    e1.fullname = 'Anand Kumar'
    print(e1.fullname)
    print(e1.email)

    del e1.fullname
    print(e1.email)