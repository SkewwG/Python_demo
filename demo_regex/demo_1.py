import re

line = '123 skeleton123'
print('line:{}'.format(len(line)))
regex_line = r'\d*\s([a-z]*)\d*'
obj = re.match(regex_line,line)
print(obj)
print(obj.group(1))
if obj:
    print('yes')