# 冒泡排序
lis = [56, 12, 1, 8, 354, 10, 100, 34, 56, 7, 23, 456, 234, -58]


# 执行结果[-58, 1, 7, 8, 10, 12, 23, 34, 56, 56, 100, 234, 354, 456]

def sortport(lis):
    for i in range(len(lis) - 1):  # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(lis) - 1 - i):  # j 为列表下标 -i目的是不与前面进行比较
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]  # 交换两个数字
    return lis

# 计算x的n次方


def power(x, n):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s

def x(lis):
    s=0
    for i in lis:
        s=i*i+s
    return s
# 改变原键值对颠倒并产生新的键值对
dict1 = {"a": "A", "b": "B", "c": "C"}
dict2 = {y: x for x, y in dict1.items()}
# print(dict2)
# print(dict1.items())

a = [35,36,3 ,"3a"]
print(a.count(3))
print(a.index(3))

