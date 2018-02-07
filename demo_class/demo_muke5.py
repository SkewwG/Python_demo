#对象的实例化

class Program():
    def __new__(cls,*args,**kwargs):
        print('创建类的对象即实例化一个对象')
        return super(Program,cls).__new__(cls)

    def __init__(self,name,age,weight):
        print('初始化对象即对象实例化')
        self.name = name
        self._age = age
        self.__weight = weight

p = Program('admin','18','96')
print(p.__dict__)

