import pytest
"""
class Bus:
    def __init__(self,passenger=None):
        if passenger is None:
            self.passenger =[]
        else:
            self.passenger=list(passenger)

    def pick(self,name):
        self.passenger.append(name)
    def drop(self,name):
        self.passenger.remove(name)



hwd=["anil","sunil","giri"]
b1 = Bus(hwd)
b1.drop("anil")
print(b1.passenger)
print(hwd)
print(vars(Bus))

"""
#hwd=["asas","asas","asasa"]
#b2 = Bus(hwd)
#b1.drop("anil")
#print(b2.passenger)
#print(hwd)


"""
from functools import wraps
no_calls =0
def count(func):
    wraps(func)
    def inner(*args,**kwargs):
        inner.no_calls += 1
        return func(*args,**kwargs)
    inner.no_calls = 0
    return inner


@count
def fib1(n):
    if n<2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

print(fib1(32))
print(fib1.no_calls)

"""

"""
def init_func(self,color):
    self.color=color

def drive(self):
    print("I am driving")


car =type("car",(object,),{
    "__init__": init_func,
    "drive": drive,
})

my_car =car("red")
print(my_car.drive())

"""

lambda x:x[::-1]






