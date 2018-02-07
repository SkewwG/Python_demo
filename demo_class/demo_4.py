class C:
    count = 0
    def __init__(self):
        C.count += 1

        print('count:{0}'.format(C.count))
    def __del__(self):
        C.count -= 1
        print('count:{0}'.format(C.count))

a = C()
b = C()
c = C()

