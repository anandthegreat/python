'''
Class variables and default arguments are created
when the function is loaded, and only once. That means
any changes to a mutable default argument or mutable
class variable are permanent

Therefore, pass None as the default param
'''

# bad func
def func(key,val,a={}):
    a[key] = val
    return a

# correct way
def func2(key,val,a=None):
    if a is None:
        a = {key: val}
    else:
        a[key] = val
    return a

print(func('a',10))
print(func('b',20))
print(func2('a',10))
print(func2('b',20))

def mutable_default_arg (something = {'foo':1}):
    something['foo'] += 1
    print (something)

mutable_default_arg()
mutable_default_arg()