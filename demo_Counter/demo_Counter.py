from collections import Counter

words1 = ['a','b','c','d','e','f','g','h','a','a','v','c','d','d','d','e','e']
words2 = ['a','b','c','d','e','f','g','h','a','s','v','c','c','d','d','f','e']
# 对可哈希的对象序列做了映射
word_count1 = Counter(words1)
print('words1 {}'.format(word_count1))
word_count2 = Counter(words2)
print('words2 {}'.format(word_count2))

# Counter对象可以加减。加就是加，减的话，减完了就没有了。
word_count_add = word_count1 + word_count2
print('word_count_add {}'.format(word_count_add))
word_count_del = word_count1 - word_count2
print('word_count_del {}'.format(word_count_del))