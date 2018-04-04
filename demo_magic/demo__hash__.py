# __hash__是hash()方法的装饰器版本。 hash()方法总是会返回int型的数字.可以用于比较一个唯一的对象
class Person1:
    def __init__(self):
        pass

p1 = Person1()
print(hash(p1))

class Person2:
    def __hash__(self):
        return 1234

p2 = Person2()
print(hash(p2))                 # 1234