def isevent(n):
    return n if n % 2 == 0 else None

a = list(map(isevent, range(10)))
print(a)

b = list(filter(isevent, range(10)))
print(b)