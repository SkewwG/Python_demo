def demo_yield(n):
    print('cunting')
    while n > 0:
        print('before')
        yield n
        n -= 1
        print('afeter')


print(demo_yield(5).__next__())