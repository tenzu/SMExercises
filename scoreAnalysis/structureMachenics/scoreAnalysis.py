# # 本程序用于分析往届《结构力学（2）》的成绩

import os
import pandas as pd
import matplotlib.pyplot as plt


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
    linestyle="-.",
    label="期望值 ± 标准差",
)
plt.axvline(df["最终成绩"].mean() - df["最终成绩"].std(), color="green", linestyle="-.")
plt.legend()
plt.show()


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# 特征和目标变量
X = df[["平时成绩", "期末成绩"]]
y = df["最终成绩"]

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=666
)

# 线性回归
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)

# 多项式回归
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)
lr_poly = LinearRegression()
lr_poly.fit(X_train_poly, y_train)
y_pred_poly = lr_poly.predict(X_test_poly)

# 决策树回归
tree = DecisionTreeRegressor(random_state=666)
tree.fit(X_train, y_train)
y_pred_tree = tree.predict(X_test)

# 支持向量回归
svr = SVR(kernel="rbf")
svr.fit(X_train, y_train)
y_pred_svr = svr.predict(X_test)

# 在一个DataFrame中存储所有模型的评价结果并打印
evaluations = pd.DataFrame(
    {
        "模型": [
            "线性回归",
            "多项式回归",
            "决策树回归",
            "支持向量回归",
        ],
        "R²": [
            r2_score(y_test, y_pred),
            r2_score(y_test, y_pred_poly),
            r2_score(y_test, y_pred_tree),
            r2_score(y_test, y_pred_svr),
        ],
        "MSE": [
            mean_squared_error(y_test, y_pred),
            mean_squared_error(y_test, y_pred_poly),
            mean_squared_error(y_test, y_pred_tree),
            mean_squared_error(y_test, y_pred_svr),
        ],
        "MAE": [
            mean_absolute_error(y_test, y_pred),
            mean_absolute_error(y_test, y_pred_poly),
            mean_absolute_error(y_test, y_pred_tree),
            mean_absolute_error(y_test, y_pred_svr),
        ],
    }
)
# 打印时每列数据左对齐
pd.set_option("display.unicode.ambiguous_as_wide", True)
pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.width", 180)
print(f"模型评价结果:\n{evaluations.to_string(index=False)}")

# 画两个子图，分别用散点图表示回归模型预测平时成绩和最终成绩的关系，回归模型预测期末成绩和最终成绩的关系
# 第一行两个子图表示线性回归结果，只画散点
plt.rcParams["font.sans-serif"] = ["STHeiti"]  # 用来正常显示中文标签
plt.rcParams["axes.unicode_minus"] = False  # 用来正常显示负号
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0][0].scatter(X_train["平时成绩"], y_train, label="训练集")
axes[0][0].scatter(X_test["平时成绩"], y_test, label="测试集")
axes[0][0].scatter(X_test["平时成绩"], y_pred, label="线性回归模型", color="red")
axes[0][0].set_xlabel("平时成绩")
axes[0][0].set_ylabel("最终成绩")
axes[0][0].set_title("线性回归模型预测期末成绩和最终成绩的关系")
axes[0][0].legend(loc="best")
axes[0][1].scatter(X_train["期末成绩"], y_train, label="训练集")
axes[0][1].scatter(X_test["期末成绩"], y_test, label="测试集")
axes[0][1].scatter(X_test["期末成绩"], y_pred, label="线性回归模型", color="red")
axes[0][1].set_xlabel("期末成绩")
axes[0][1].set_ylabel("最终成绩")
axes[0][1].set_title("线性回归模型预测期末成绩和最终成绩的关系")
axes[0][1].legend(loc="best")
# 第二行两个子图表示支持向量回归结果，只画散点
axes[1][0].scatter(X_train["平时成绩"], y_train, label="训练集")
axes[1][0].scatter(X_test["平时成绩"], y_test, label="测试集")
axes[1][0].scatter(
    X_test["平时成绩"], y_pred_svr, label="支持向量回归模型", color="red"
)
axes[1][0].set_xlabel("平时成绩")
axes[1][0].set_ylabel("最终成绩")
axes[1][0].set_title("支持向量回归模型预测期末成绩和最终成绩的关系")
axes[1][0].legend(loc="best")
axes[1][1].scatter(X_train["期末成绩"], y_train, label="训练集")
axes[1][1].scatter(X_test["期末成绩"], y_test, label="测试集")
axes[1][1].scatter(
    X_test["期末成绩"], y_pred_svr, label="支持向量回归模型", color="red"
)
axes[1][1].set_xlabel("期末成绩")
axes[1][1].set_ylabel("最终成绩")
axes[1][1].set_title("支持向量回归模型预测期末成绩和最终成绩的关系")
axes[1][1].legend(loc="best")
plt.show()
