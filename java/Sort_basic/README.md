冒泡、选择、插入都需要 O(N^2) 时间级别。一般不会选择冒泡排序，平均性能没有选择排序和插入排序好。

选择排序把交换次数降低到最低，但是比较次数还是挺大的。当数据量小，并且交换数据相对于比较数据更加耗时的情况下，用选择排序。

在大多数情况下，假设数据量比较小或基本有序时，插入排序是三种算法中最好的选择。
