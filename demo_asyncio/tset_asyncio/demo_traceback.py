# format_exc()返回字符串，print_exc()则直接给打印出来。
# 即traceback.print_exc()与print(traceback.format_exc())效果是一样的。
# print_exc()还可以接受file参数直接写入到一个文件。比如: traceback.print_exc(file=open('tb.txt','w+'))
import traceback
import time

print('start')

time.sleep(1)

try:
    1/0
except Exception as e:
    print(traceback.format_exc())

time.sleep(1)

try:
    1/0
except Exception as e:
    traceback.print_exc()

time.sleep(1)

print('end!')