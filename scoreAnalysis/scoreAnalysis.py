'''
本程序用于分析往届《结构力学（2）》的成绩
'''

# Version 1.0, 顺序执行代码完成对应功能

import os
# import numpy as np
import matplotlib.pyplot as plt

# 获取当前 Python 文件所在的目录
current_path = os.path.dirname(os.path.abspath(__file__))

# 列出当前路径下的所有文件
files = os.listdir(current_path)

# 用于存储读入数据的总列表
data = []
# 用于存储学期的列表
semesters = []

# 遍历所有文件，仅列出后缀名为txt的文件
for file in files:
    if file.endswith('.txt'):