import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split

# 説明変数と目的変数の準備
df = pd.read_csv("./test_dataset.csv")
xcol = list( df.columns[:3] )
label = df.columns[3]
x = df[xcol]
t = df[label]

# 決定木によるモデルの定義
model = tree.DecisionTreeClassifier(max_depth=10, random_state=0)

# 訓練データ(70%)と検証データ(30%)の用意
x_train, x_test, y_train, y_test = train_test_split(x, t, test_size = 0.3, random_state = 0)

# モデルの学習
model.fit(x_train, y_train)

# モデルの検証
score = model.score(x_test, y_test) # score: 0.9942196531791907
print(f"Score: {score}")

# モデルの保存
import pickle
with open('color-classification-model_tree.pkl', 'wb') as f:
 pickle.dump(model, f)