# -*- coding:utf-8 -*-
# @Time  : 2019/6/24 21:41
# @Author: Zhou JD
# @File  : baotu.py

import requests
from lxml import etree

# 1 请求包图网源代码
response = requests.get("https://ibaotu.com/shipin/")
# print(response.text)
html = etree.HTML(response.text)
# 2 抽取视频标题、视频链接
tit_list = html.xpath('//span[@class="video-title"]/test()')
# 3 下载视频 保存视频

