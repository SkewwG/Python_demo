
'''
format(...)
    # 格式换字符串输出（方法与%相似，但可以指定顺序）
    S.format(*args, **kwargs) -> str

    Return a formatted version of S, using substitutions from args and kwargs.
    The substitutions are identified by braces ('{' and '}').

None
'''
print(help(str.format))
name = 'StivenWang'
fruit = 'apple'
a = 'my name is {},I like {}'.format(name,fruit)
b = 'my name is {1},I like {0}'.format(fruit,name)
c = 'my name is {mingzi},I like {shuiguo}'.format(shuiguo=fruit,mingzi=name)
print(a)                        # my name is StivenWang,I like apple
print(b)                        # my name is StivenWang,I like apple
print(c)                        # my name is StivenWang,I like apple
