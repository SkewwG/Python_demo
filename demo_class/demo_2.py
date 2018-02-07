#钻石继承

class A:
    def __init__(self):
        print('into A')
        print('out A')

class B(A):
    def __init__(self):
        print('into B')
        super().__init__()
        print('out B')

class C(A):
    def __init__(self):
        print('into C')
        super().__init__()
        print('out C')


class D(B,C):
    def __init__(self):
        print('into D')
        super().__init__()
        print('out D')

d = D()
