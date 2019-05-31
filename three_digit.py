# -*- coding:utf-8 -*-
# @Time  : 2019/4/27 21:21
# @Author: Zhou JD
# @File  : three_digit.py
# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
num = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if(i != j) and (j != k) and(i != k):
                print(i*100+j*10+k)
                num = num+1
print("共能组成", num, "个数")
