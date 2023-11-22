import matplotlib.pyplot as plt
import pandas
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pandas.read_json("../data/data.json")

d = {'Rock': 0, 'Pop': 1, 'Pop Rock': 2, 'Alternative Rock':3, 'Flamenco':4, 'Electronic':5}
df['gender'] = df['gender'].map(d)

features = ['year']

x = df[features]
y = df['gender']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

train_tree = DecisionTreeClassifier()
train_tree = train_tree.fit(x_train, y_train)

tree.plot_tree(train_tree, feature_names=features)

plt.show()

test_tree = DecisionTreeClassifier()
test_tree = test_tree.fit(x_test, y_test)

tree.plot_tree(test_tree, feature_names=features)

plt.show()