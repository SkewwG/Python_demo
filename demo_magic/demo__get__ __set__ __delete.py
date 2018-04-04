# 要想成为一个描述符，一个类必须具有实现 __get__ , __set__ 和 __delete__ 三个方法中至少一个。
# 即：只要定义了__get__ , __set__ 和 __delete__ 三个方法中的一个，那么这个类就是描述符
# instance是实例本身，owner是类本身
# value是传递的值
# __get__有return是因为当你用print打印的时候，可以打印return的结果
# __set__无需return，因为赋值后，无法print
class Descriptor:
    def __get__(self, instance, owner):
        print('__get__() called')
        return '__get__()', instance, owner

    def __set__(self, instance, value):
        print('__set__() called', instance, value)

    def __delete__(self, instance):
        print('__delete__() called')


class T:
    d = Descriptor()

t = T()

print(t.d)          # __get__() called          ('__get__()', <__main__.T object at 0x0000000004EDE4E0>, <class '__main__.T'>)
print(T.d)          # __get__() called          ('__get__()', None, <class '__main__.T'>)
t.d = 'aaa'         # __set__() called          <__main__.T object at 0x00000000048CE4E0> aaa
del t.d             # __delete__() called
