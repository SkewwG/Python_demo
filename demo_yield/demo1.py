def count(n):
    print ("cunting" )
    while n > 0:
        print ('before yield')
        yield n   #生成值：n
        n -= 1
        print ('after yield' )

c = count(5)
c.__next__()