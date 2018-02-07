#鱼池里乌龟和鱼的数量

class Turtle:
    def __init__(self,x):
        self.x = x

class Fish:
    def __init__(self,y):
        self.y = y

class Pool:
    def __init__(self,x,y):
        self.tutle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print('tutle:{0}\nfish:{1}'.format(self.tutle.x,self.fish.y))

p = Pool(3,4)
p.print_num()