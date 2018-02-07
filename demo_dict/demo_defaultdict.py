# 一键多值字典
from collections import defaultdict

# 相当于列表形式的字典。该字典可以使用列表的方法，且值可以重复
dictList = defaultdict(list)
dictList['a'].append(1)
dictList['a'].append(2)
dictList['a'].append(2)
dictList['b'].append(3)
print(dictList['a'])            # [1, 2, 2]

# 相当于集合形式的字典。该字典可以使用集合的方法，且值不可以重复
dictSet = defaultdict(set)
dictSet['a'].add(1)
dictSet['a'].add(2)
dictSet['a'].add(2)
dictSet['b'].add(3)
print(dictSet['a'])             # {1, 2}