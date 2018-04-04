# repr面向机器，产生机器可读的输出
# str面向人。产生人类可读的输出
class Person:
    def __str__(self):
        return '__str__() is called'

    def __repr__(self):
        return '__repr__() is called'

p = Person()
print(str(p))
print(repr(p))
print(p)            # __str__() is called  可以看出默认调用的是__str__