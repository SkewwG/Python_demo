def foo(x):
    print("executing foo(%s)" %(x))

class A:
    # 实例方法
    def foo(self,x):
        print("executing foo(%s,%s)" %(self,x))

    # 类方法
    @classmethod
    def class_foo(cls,x):
        print("executing class_foo(%s,%s)" %(cls,x))

    # 静态方法
    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" %x)

a = A()
foo(0)
a.foo(1)
a.class_foo(2)
a.static_foo(3)

