# 有趣且有用的工具集合

## [1.annoy index](annoy_index.py)
参考博客：[快速计算距离Annoy算法原理及Python使用](https://blog.csdn.net/m0_37850187/article/details/92712490)
内部原理：
	①建立索引：
		随机算着两点，执行聚类数为2的kmeans的过程
		经过多次迭代，最终原始数据会形成一棵二叉树【叶子节点：数据点，中间节点：分割超平面】
	②查询过程：
		在二叉树中进行数据检索【可能会用到优先队列等其他数据结构帮助返回TOP N的数据】
API简介：

- AnnoyIndex(f, metric='angular') 初始化新的索引树，元素向量维度为f. Metric 可以是 “angular”, “euclidean”, “manhattan”, “hamming”, or “dot”.
- a.add_item(i, v) 添加向量元素v到索引树，其中，i应该为非负整数
- a.build(n_trees) 建立索引树，n_trees表示所建树的个数。树的个数更多，则精度更高，但也要考虑到效率，建立索引树比较耗费时间，一般n_trees=100均能满足精度要求
- a.save(fn, prefault=False) 保存模型到磁盘上fn表示文件路径
- a.load(fn, prefault=False)下来模型进行计算，loads (mmaps) an index from disk. If prefault is set to True, it will pre-read the entire file into memory (using mmap with MAP_POPULATE). Default is False.
- a.get_nns_by_item(i, n, search_k=-1, include_distances=False)使用item索引号进行计算,i表示item索引号， n表示计算要得到的最近邻的item个数
- a.get_item_vector(i):返回之前添加的item索引号i所对应的向量
- a.get_n_items() 返回整个索引树中item的数量
- a.get_n_trees() 返回整个索引树中树的个数
- a.get_nns_by_vector(v, n, search_k=-1, include_distances=False) 使用item向量v进行计算
- a.on_disk_build(fn)将索引树建立到具体文件上，这样建立完树后就不用手动保存

实现：
	[annoy_test.py](annoy_test.py)

​		
