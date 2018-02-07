'''
UUID是128位的全局唯一标识符，通常由32字节的字母串表示。它可以保证时间和空间的唯一性，也称为GUID。

全称为：UUID--Universally Unique IDentifier  在python 中叫做UUID，在C#中称为 GUID--Globally Unique IDentifier.

它通过MAC地址，时间戳，命名空间，随机数，伪随机数来保证生成ID的唯一性。

　　UUID主要有五个算法，也就是五种方法来实现。

（1）. uuid1()---基于时间戳

　　由MAC地址，当前时间戳，随机数字生成。可以保证全球范围内的唯一性。但是由于MAC地址的使用同时带来了安全问题，

局域网中可以使用IP来代替MAC。

（2）. uuid2()---基于分布式计算环境DCE（python中没有这个函数）

　　算法和uuid1相同，不同的是把时间戳的前4位换位POSIX的UID，实际中很少用到该方法。

（3）. uuid3()---基于名字和MD5散列值

　　通过计算名字和命名空间的MD5散列值得到，保证了同一命名空间中不同名字的唯一性，和不同命名空间的唯一性，

但同一命名空间的名字生成相同的uuid。

（4）. uuid4()---基于随机数

　　由伪随机数得到，有一定的重复概率，该概率可以计算出来。

（5）. uuid5()---基于名字的SHA-1散列值

　　算法和uuid3()相同，不同的是使用Secure Hash Algorithm 1 算法。
'''
import uuid

print('uuid1 = {}'.format(uuid.uuid1()))
#print('uuid3 = {}'.format(uuid.uuid3()))
print('uuid4 = {}'.format(uuid.uuid4()))