# -*- coding:utf-8 -*-
# @Time  : 2019/2/23 21:43
# @Author: Zhou jundong
# @File  : fruit_machine.py

import tkinter
import threading
import time


root = tkinter.Tk()
root.title("水果转盘")
root.minsize(300, 300)

# 创建按钮
bth1 = tkinter.Button(root, text="苹果", bg="red")
bth1.place(x=20, y=20, width=50, height=50)

bth2 = tkinter.Button(root, text="橘子", bg="red")
bth2.place(x=90, y=20, width=50, height=50)

bth3 = tkinter.Button(root, text="香蕉", bg="red")
bth3.place(x=160, y=20, width=50, height=50)

bth4 = tkinter.Button(root, text="芒果", bg="red")
bth4.place(x=230, y=20, width=50, height=50)

bth5 = tkinter.Button(root, text="西瓜", bg="red")
bth5.place(x=20, y=90, width=50, height=50)

bth6 = tkinter.Button(root, text="草莓", bg="red")
bth6.place(x=20, y=160, width=50, height=50)

bth7 = tkinter.Button(root, text="樱桃", bg="red")
bth7.place(x=20, y=230, width=50, height=50)

bth8 = tkinter.Button(root, text="柚子", bg="red")
bth8.place(x=90, y=230, width=50, height=50)

bth9 = tkinter.Button(root, text="榴莲", bg="red")
bth9.place(x=160, y=230, width=50, height=50)

bth10 = tkinter.Button(root, text="葡萄", bg="red")
bth10.place(x=230, y=230, width=50, height=50)

bth11 = tkinter.Button(root, text="橙子", bg="red")
bth11.place(x=230, y=160, width=50, height=50)

bth12 = tkinter.Button(root, text="荔枝", bg="red")
bth12.place(x=230, y=90, width=50, height=50)

# 将所有按钮添加到列表
fruitLists = [bth1, bth2, bth3, bth4, bth5, bth6, bth7, bth8, bth9, bth10, bth11, bth12]
isloop = False   # 是否循环
stop = False     # 停止
stopid = None    # 循环组件id


def round():
    global isloop
    global stopid

    if isloop == True:
        return
    i = 0
    if isinstance(stopid, int):
        i = stopid

    while True:
        time.sleep(0.01) # 延迟
        # 将所有组件背景变成白色
        for x in fruitLists:
            x["bg"] = "pink"
        fruitLists[i]["bg"] = "yellow"
        i += 1
        print("当前i是：", i)

        if i >= len(fruitLists):
            i = 0
        if stop == True:
            isloop = False
            stopid = 0
            break

# 停止
def stop1():
    global stop

    if stop == True:
        return
    stop = True


# 建立一个新线程
def network():
    global isloop
    global stop

    stop = False

    t = threading.Thread(target=round)
    t.start()
    isloop = True

# 开始按钮
btn_start = tkinter.Button(root, text="start", command=network, bg="red")
btn_start.place(x=90, y=125, width=50, height=50)

# 停止按钮
btn_stop = tkinter.Button(root, text="stop", command=stop1, bg="red")
btn_stop.place(x=160, y=125, width=50, height=50)

root.mainloop()
