class employer:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

emp = employer('ske',100)
print('name:{0}\nsalary:{1}'.format(emp.name,emp.salary))