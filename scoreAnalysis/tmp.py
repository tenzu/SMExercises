# # 本程序用于分析往届《结构力学（2）》的成绩

import os
import pandas as pd
from matplotlib import pyplot as plt
import myMlModule as mmm


path = "./"
files = os.listdir(path)

# 定义读入文件生成 DataFrame 的函数


# 定义读入单个文件生成 DataFrame 的函数
def readFile(fileName):
    df = pd.read_csv(fileName, sep="\t")
    return df


# 定义读入全部文件生成 DataFrame 的函数
def readFiles(files):
    df = pd.DataFrame()
    for file in files:
        # 判断文件是否以 .txt 结尾
        if file.endswith(".txt"):
            df = pd.concat([df, readFile(file)])
    return df


# 输入1：读入指定文件名的文件，输入2：读入全部文件，输入其他内容退出程序
def main():
    print("可选择的文件名包括:")
    readFileNames = [file.split(".")[0] for file in files if file.endswith(".txt")]
    for fileName in readFileNames:
        print(fileName)
    print("输入1：读入指定文件名的文件，输入2：读入全部文件，输入其他内容退出程序")
    choice = input()
    if choice == "1":
        fileName = input("请输入文件名：") + ".txt"
        df = readFile(fileName)
    elif choice == "2":
        df = readFiles(files)
    else:
        exit()
    return df

# 一次性读入全部文件
df = readFiles(files)

# 导入 myMlModule 模块，初始化 MLPipeline 对象
mlp = mmm.MLPipeline(df, "期末成绩", test_size=0.2, random_state=42)
# 选用线性回归模型
mlp.train_model("LinearRegression")
# 评估线型回归模型
mlp.get_best_model()
# 绘制模型预测值和真实值的散点图
mlp.plot_predictions()

# 绘制模型的特征重要性
mlp.plot_feature_importance()