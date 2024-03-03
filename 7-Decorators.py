import time
from functools import wraps

# Higher order function
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"Function {func.__name__} ran in {t2} seconds")
        return res
    return wrapper

def logger(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        res = func(*args, **kwargs)
        with open(f'{func.__name__}.txt','a+') as f:
            f.write(f'Function {func.__name__} returned value {res}')
        return res
    return wrapper

# If we stack decorators, then the decorator closer to
# function is applied first, since it will return wrapper
# the next decorator in stack will have function as "wrapper"
# therefore we use @wraps from functools
@logger
@timer
def my_func():
    time.sleep(3)
    return "Hello world"

def my_func2(a,b):
    time.sleep(2)
    return a+b

if __name__ == '__main__':
    print(my_func())

    # Same as applying @timer decorator
    decorated_myfunc2 = timer(my_func2)
    print(decorated_myfunc2(1,2))
