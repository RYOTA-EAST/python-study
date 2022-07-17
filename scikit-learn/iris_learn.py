import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score

df = pd.read_csv('iris.csv')

# データを解析用と回答に分ける
X = df[['SepalLengthCm', 'SepalWidthCm',
        'PetalLengthCm', 'PetalWidthCm']]
y = df['Species']


# Xとｙを解析用とテスト用に分ける
X_train, X_test, y_train, y_test = train_test_split(
  X, y, test_size=0.1, random_state=77
)

print(X_train.columns.values, y)
print("X_test", X_test)

# 学習
clf = RandomForestClassifier(random_state=77)

clf.fit(X_train, y_train)

# 予測
pred = clf.predict(X_test)
print(pred)

# 評価
accuracy = accuracy_score(y_test, pred)
print("正解率は", accuracy * 100, "%です")

# 学習済みモデルを使う
print(clf.predict([[7.4,2.8,6.1,1.9]]))