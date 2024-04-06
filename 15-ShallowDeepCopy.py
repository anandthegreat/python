import copy
'''
Concept:
    1) Shallow copy: it is only one level deep. Objects deeper than 1 level
       are referenced and not copied. Therefore, modifiying one complex object
       modifies the other which is shallow copied.
       Eg. a = [[1,2,3],4,5]
           b = copy.copy(a)
           a[0][0] = 100
           Then b[0][0] also becomes 100, but a[1] = 400 doesn't make 
           b[1] as 400 as its level 1
    2) Deep Copy: it is a complete recursive copy of the object. 
        Disadvantage is that its slower than shallow copy
'''

class Pair:
    def __init__(self,a,b,c=[]):
        self.a = a
        self.b = b
        self.c = [[a,b],a,b]

if __name__ == '__main__':

    # wrong way of copying mutable objects (lists/sets/dictionaries)
    a = [1,2,3]
    b = a       # b is just a reference to a
    a[0] = 5    # will make b[0] = 5 as well
    print(b)    # [5,2,3]
    print(a is b)  # True

    # correct way of (shallow) copying
    a = [1,2,3]
    b = list(a)  # or set(a) or dict(a)
    print(a is b)    # False, both are diff objects
    a[0] = 5
    print(b)    # [1,2,3] Yay!

    # dealing with complex objects
    x = [1,2,[3,4,5],6]
    y = copy.copy(x)
    x[2][1] = 300
    print(y[2][1])  # 300, due to shallow copy
    y = copy.deepcopy(x)
    x[2][1] = 600
    print(y[2][1]) # still 300, correct!

    # copying class instances - wrong way
    p1 = Pair(1,2)
    p2 = p1      # p2 is just a reference to p1
    p1.a = 100   # p2 is also modified
    print(p2.a)  # becomes 100

    # copying class instances - shallow way (wrong)
    p2 = copy.copy(p1)
    print(id(p1),id(p2))  # different ids
    p1.c.append('fellow')
    print(p1.c)
    print(p2.c)    # modified

    # copying class instances - correct way
    p2 = copy.deepcopy(p1)
    print(id(p1), id(p2))  # different ids
    p1.c.append('hello')
    print(p1.c)
    print(p2.c)  # not modified