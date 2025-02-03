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


df = main()
# print(df.head())

# 重新生成 index 从 0 开始
df = df.reset_index(drop=True)
len1 = len(df)
# 清洗数据
# 去除”期末成绩“不是数字的行
df = df[pd.to_numeric(df["期末成绩"], errors="coerce").notnull()]
# 将”期末成绩“、”平时成绩“、”最终成绩“转换为数值型
df["期末成绩"] = pd.to_numeric(df["期末成绩"], errors="coerce")
df["平时成绩"] = pd.to_numeric(df["平时成绩"], errors="coerce")
df["最终成绩"] = pd.to_numeric(df["最终成绩"], errors="coerce")
len2 = len(df)
print(f"初始数据一共有 {len1} 条，清洗后一共有 {len2} 条数据")

# 当前有效成绩总数
print(f"当前有效成绩共 {len2} 条记录")
# 列出平时成绩平均值和标准差，列出总评成绩平均值和标准差，列出最终成绩平均值和标准差
print(
    f"平时成绩：平均值 = {df["平时成绩"].mean():.2f}, 标准差 = {df["平时成绩"].std():.2f}"
)
print(
    f"期末成绩：平均值 = {df["期末成绩"].mean():.2f}, 标准差 = {df["期末成绩"].std():.2f}"
)
print(
    f"最终成绩：平均值 = {df["最终成绩"].mean():.2f}, 标准差 = {df["最终成绩"].std():.2f}"
)

# 绘制最终成绩直方图，显示均值、方差、标准差
plt.rcParams["font.sans-serif"] = ["STHeiti"]  # 用来正常显示中文标签
plt.hist(df["最终成绩"], bins=25, edgecolor="black", histtype="bar", alpha=0.7)
plt.xlabel("最终成绩")
plt.ylabel("学生数量")
plt.title("最终成绩分布图")
plt.axvline(df["最终成绩"].mean(), color="red", linestyle="--", label="期望值")
plt.axvline(
    df["最终成绩"].mean() + df["最终成绩"].std(),
    color="green",
    linestyle="--",
    label="期望值 ± 标准差",
)
plt.axvline(df["最终成绩"].mean() - df["最终成绩"].std(), color="green", linestyle="--")
plt.legend()
plt.show()

# 采用决策树回归算法根据平时成绩预测期末成绩
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

# 划分训练集和测试集
X = df[["平时成绩"]]
y = df[["期末成绩"]]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.05, shuffle=True, random_state=42
)


# 定义预测函数
def predict(X_train, X_test, y_train, y_test):
    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    return y_pred


# 评估模型效果
from sklearn.metrics import mean_squared_error, r2_score


def evaluate(y_test, y_pred):
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"均方误差 (MSE) = {mse:.2f}")
    print(f"决定系数 (R^2) = {r2:.2f}")


# 调用预测函数和评估函数
y_pred = predict(X_train, X_test, y_train, y_test)
evaluate(y_test, y_pred)

# 计算平时成绩和期末成绩的相关系数
corr = df[["平时成绩", "期末成绩"]].corr().iloc[0, 1]
print(f"平时成绩和期末成绩的相关系数为 {corr:.2f}")

# 绘制平时成绩和期末成绩散点图
plt.scatter(df["平时成绩"], df["期末成绩"], alpha=0.7)
plt.xlabel("平时成绩")
plt.ylabel("期末成绩")
plt.title("平时成绩和期末成绩散点图")
plt.show()
