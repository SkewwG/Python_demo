def gen_one():
    subgen = range(10)
    yield from subgen

def gen_two():
    subgen = range(10)
    for item in subgen:
        yield item

r = gen_one()
print(r.__next__())
print(r.__next__())