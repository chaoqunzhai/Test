
"""
class Foo(object):
    _i = None

    @classmethod
    def instance(cls):
        if cls._i:
            return cls._i
        else:
            obj = Foo()
            cls._i = obj
            return cls._i

# obj = Foo()
# obj = Foo()
# obj = Foo()
obj1 = Foo.instance()
obj2 = Foo.instance()
"""

class Foo(object):
    _i = None
    def __init__(self):
        self.n = 123
    def __new__(cls, *args, **kwargs):
        if cls._i:
            return cls._i
        else:
            o = object.__new__(cls,*args, **kwargs)
            cls._i = o
            return cls._i

obj1 = Foo()
obj2 = Foo()
obj3 = Foo()
print(obj1,obj2,obj3)




