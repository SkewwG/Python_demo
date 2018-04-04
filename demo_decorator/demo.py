# 装饰器

def func1(func):
    print('func1')
    def func2():
        print('func2')
        func()
    func2()

@func1
def func3():
    print('func3')

