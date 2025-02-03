import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.svm import SVR, SVC
from sklearn.metrics import mean_squared_error, accuracy_score

class MLPipeline:
    def __init__(self, data, target_column, test_size=0.2, random_state=42):
        """
        初始化类
        :param data: 输入数据 (Pandas DataFrame)
        :param target_column: 目标列的名称
        :param test_size: 测试集比例
        :param random_state: 随机种子
        """
        self.data = data
        self.target_column = target_column
        self.test_size = test_size
        self.random_state = random_state
        self.X_train, self.X_test, self.y_train, self.y_test = self._split_data()
        self.preprocessor = self._build_preprocessor()
        self.models = {
            'LinearRegression': LinearRegression(),
            'DecisionTreeRegressor': DecisionTreeRegressor(random_state=random_state),
            'RandomForestRegressor': RandomForestRegressor(random_state=random_state),
            'SVR': SVR(),
            'LogisticRegression': LogisticRegression(random_state=random_state),
            'DecisionTreeClassifier': DecisionTreeClassifier(random_state=random_state),
            'RandomForestClassifier': RandomForestClassifier(random_state=random_state),
            'SVC': SVC(random_state=random_state)
        }
        self.results = {}

    def _split_data(self):
        """
        划分数据集为特征和目标变量，并拆分为训练集和测试集
        """
        X = self.data.drop(columns=[self.target_column])
        y = self.data[self.target_column]
        return train_test_split(X, y, test_size=self.test_size, random_state=self.random_state)

    def _build_preprocessor(self):
        """
        构建数据预处理管道
        """
        numeric_features = self.X_train.select_dtypes(include=['int64', 'float64']).columns
        categorical_features = self.X_train.select_dtypes(include=['object', 'category']).columns

        numeric_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='mean')),  # 缺失值填充
            ('scaler', StandardScaler())  # 标准化
        ])

        categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),  # 缺失值填充
            ('onehot', OneHotEncoder(handle_unknown='ignore'))  # 独热编码
        ])

        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numeric_features),
                ('cat', categorical_transformer, categorical_features)
            ])

        return preprocessor

    def train_model(self, model_name):
        """
        训练指定模型
        :param model_name: 模型名称 (必须是 self.models 中的键)
        """
        if model_name not in self.models:
            raise ValueError(f"Model '{model_name}' not found in available models.")

        # 创建完整的管道：预处理 + 模型
        model_pipeline = Pipeline(steps=[
            ('preprocessor', self.preprocessor),
            ('model', self.models[model_name])
        ])

        # 训练模型
        model_pipeline.fit(self.X_train, self.y_train)

        # 预测并评估
        y_pred = model_pipeline.predict(self.X_test)
        if model_name in ['LinearRegression', 'DecisionTreeRegressor', 'RandomForestRegressor', 'SVR']:
            mse = mean_squared_error(self.y_test, y_pred)
            self.results[model_name] = mse
            print(f"{model_name} - Mean Squared Error: {mse:.4f}")
        else:
            accuracy = accuracy_score(self.y_test, y_pred)
            self.results[model_name] = accuracy
            print(f"{model_name} - Accuracy: {accuracy:.4f}")

    def get_best_model(self):
        """
        返回表现最好的模型
        :return: 最佳模型名称和对应的评估指标
        """
        if not self.results:
            raise ValueError("No models have been trained yet.")
        if 'LinearRegression' in self.results:  # 回归任务
            best_model = min(self.results, key=self.results.get)
        else:  # 分类任务
            best_model = max(self.results, key=self.results.get)
        return best_model, self.results[best_model]

"""
# 示例使用
if __name__ == "__main__":
    # 加载示例数据集
    from sklearn.datasets import load_iris, load_diabetes

    # 分类任务示例
    iris = load_iris()
    iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
    iris_df['target'] = iris.target
    ml_pipeline = MLPipeline(iris_df, target_column='target')
    ml_pipeline.train_model('LogisticRegression')
    ml_pipeline.train_model('RandomForestClassifier')
    best_model, best_score = ml_pipeline.get_best_model()
    print(f"\nBest Model: {best_model} with Score: {best_score:.4f}")

    # 回归任务示例
    diabetes = load_diabetes()
    diabetes_df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
    diabetes_df['target'] = diabetes.target
    ml_pipeline = MLPipeline(diabetes_df, target_column='target')
    ml_pipeline.train_model('LinearRegression')
    ml_pipeline.train_model('RandomForestRegressor')
    best_model, best_score = ml_pipeline.get_best_model()
    print(f"\nBest Model: {best_model} with Score: {best_score:.4f}")
    """