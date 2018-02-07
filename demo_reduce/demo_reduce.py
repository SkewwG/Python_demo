from functools import reduce
from operator import mul
a = reduce(mul, (1, 2, 3, 4, 5))
print(a)