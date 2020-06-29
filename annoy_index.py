# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 12:57
# @Author  : Wang Sheng
# @File    : annoy_index.py.py
# @Software: PyCharm
# @function: Annoy Index


from annoy import AnnoyIndex
import random

# 指定item的为维度，如果加载词向量的话，可以变成词向量的维度
f = 40
t = AnnoyIndex(f)
for i in range(1000):
    v = [random.gauss(0, 1) for z in range(f)]
    t.add_item(i, v)

t.build(10)   # 10 trees
t.save('test.ann')

u = AnnoyIndex(f)
u.load('test.ann')  # super fast, will just mmap the file
print(u.get_nns_by_item(0, 1000))  # will find the 1000 nearest neighbors
