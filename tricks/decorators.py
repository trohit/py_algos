# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 10:49:37 2022

@author: talukr

https://towardsdatascience.com/the-simplest-tutorial-for-python-decorator-dadbf8f20b0f
"""
import random
# decorator

def traceit(func):
    def wrapped_func(*args, **kwargs):
        # __name__ introduced in py3 to disp func name
        print(f"Getting into {func.__name__}")
        func(*args, **kwargs)
        # __qualnane__ gives more info, useful for method from an obj/class
        print(f"Exiting {func.__qualname__}")
    res = wrapped_func
    # f = lambda x:x+1
    # return f(1)
    print(type(res))
    return res

class a:
    def traceit_from_class_method(func):
        def wrapped_func(*args, **kwargs):
            print(f"Getting into {func.__name__}")
            func(*args, **kwargs)
            print(f"Exiting {func.__qualname__}")
        res = wrapped_func
        # f = lambda x:x+1
        # return f(1)
        print(type(res))
        return res
    
# @a.traceit
@traceit
def foo(a):
    print(f"a:{a}")
# main
if __name__ == "__main__":
    a = random.sample(range(50), 10)
    foo(a)
    
