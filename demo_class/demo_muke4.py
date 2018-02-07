#多态
class Program():
    hobby = 'Play program'

    def __init__(self,name,age,weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def self_introduction(self):
        return 'My name is {0},I am {1} years old!'.format(self.name,self._age)

class son1_Program(Program):
    def __init__(self,name,age,weight,language):
        super(son1_Program,self).__init__(name,age,weight)
        self.language = language

    def self_introduction(self):
        return 'My name is {0},I am {1} years old!I love {2}'.format(self.name, self._age,self.language)

class son2_Program(Program):
    def __init__(self,name,age,weight,language):
        super(son2_Program,self).__init__(name,age,weight)
        self.language = language

    def self_introduction(self):
        return 'My name is {0},I am {1} years old!I love {2}'.format(self.name, self._age, self.language)

def introduction(program):
    if isinstance(program,Program):
        print(program.self_introduction())

p = Program('admin','18','96')
s1 = son1_Program('admin','18','96','Python')
s2 = son2_Program('admin','18','96','Java')

introduction(p)
introduction(s1)
introduction(s2)




