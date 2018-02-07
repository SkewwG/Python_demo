#yield的小案例
def createGenerator():
    mylist = range(1,5)
    for i in mylist:
        yield i*i
        print('i = ',i)

c = createGenerator()
for j in c:
    print('i*i = ',j)                #在此处迭代
    print('-'*20,'分割线','-'*20)


'''
yield 相当于return
1               程序运行到yild i*i时，返回的是i*i结果。并不执行yield后面的语句。
4
9
16
'''