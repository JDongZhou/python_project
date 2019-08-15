# -*- coding:utf-8 -*-
# @Time  : 2019/6/9 14:58
# @Author: Zhou JD
# @File  : file_tutorial.py
import os
fo = open("re.txt", "r+")
s = fo.read(10)  # 参数是要从已打开文件中读取的字节计数
print("读取的字符串是：", s)

position = fo.tell()  # 查找当前位置
print("当前位置是：", position)

position = fo.seek(2, 0)  # 第一个参数为要移动的字节数；第二个参数为开始移动字节的参考位置，只能为0，1，2
s = fo.read(3)
print("重新读入的字符串：", s)
fo.close()

os.rename("re.txt", "new.txt")
os.remove("new.txt")
os.mkdir("newdir")
os.chdir("/home/newdir")  # 改变当前的目录
os.getcwd()  # 当前目录
os.rmdir("/tmp/test")
