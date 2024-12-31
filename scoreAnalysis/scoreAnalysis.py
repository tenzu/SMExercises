'''
本程序用于分析往届《结构力学（2）》的成绩
'''

# Version 1.0, 顺序执行代码完成对应功能

import os
import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt

# 获取当前 Python 文件所在的目录
current_path = os.path.dirname(os.path.abspath(__file__))

# 列出当前路径下的所有文件
files = os.listdir(current_path)

# 定义空的 DataFrame
df = pd.DataFrame()

# 依次读取所有txt文件，并将数据添加到 DataFrame 中
for file in files:
    if file.endswith('.txt'):
        # 读取文件内容，跳过第一行，按空格分割
        with open(os.path.join(current_path, file), 'r') as f:
            lines = f.readlines()[1:]
            data = [line.strip().split() for line in lines]
            # 每行数据从第一列数字起分别表示：序号，学号，姓名，修读类别，期末成绩，平时成绩，总评成绩，最终成绩，绩点，是否通过，状态
            pd_data = pd.DataFrame(data, columns=['序号', '学号', '姓名', '修读类别', '期末成绩', '平时成绩', '总评成绩', '最终成绩', '绩点', '是否通过', '状态'])
            # 最后增加一列表示学期号
            pd_data['学期号'] = file.split('.')[0]
            # 将 DataFrame 合并到总的 DataFrame 中
            df = pd.concat([df, pd_data], ignore_index=True)

# 打印前3行和后3行数据
# print(df.head(3))
# print(df.tail(3))

while True:
    # 选择需要分析的学期号
    print('请选择需要分析的学期号：')
    for i in range(len(df['学期号'].unique())):
        print(f'{i+1}. {df["学期号"].unique()[i]}')
    choice = input()
    if choice.isdigit() and int(choice) in range(1, len(df['学期号'].unique())+1):
        break
    else:
        print('输入有误，请重新输入！')

# 选择的学期号
selected_semester = df['学期号'].unique()[int(choice)-1]

# 筛选出该学期的数据
semester_data = df[df['学期号'] == selected_semester]

# 打印最终成绩最小值、最大值
print(f'该学期的最终成绩最小值：{semester_data["最终成绩"].min()}')
print(f'该学期的最终成绩最大值：{semester_data["最终成绩"].max()}')

# 绘制最终成绩分布直方图
plt.hist(semester_data['最终成绩'], bins=10, edgecolor='black', linewidth=1.2)
plt.xlabel('最终成绩')
plt.ylabel('人数')
plt.title(f'该学期的最终成绩分布直方图（{selected_semester}）')
plt.show()