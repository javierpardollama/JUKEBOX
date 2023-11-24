import matplotlib.pyplot as plt
import pandas
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pandas.read_json("../data/data.json")

df = df.dropna()

d = { False: 0, True: 1}
df['bought'] = df['bought'].map(d)

features = ['likes']

x = df[features]
y = df['bought']


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

train_random_forest = RandomForestClassifier(n_estimators=5)
train_random_forest = train_random_forest.fit(x_train, y_train)

fig, axes = plt.subplots(nrows=1, ncols=train_random_forest.n_estimators, figsize=(20, 4), dpi=900)
for index in range(0, train_random_forest.n_estimators):
    tree.plot_tree(train_random_forest.estimators_[index],
                   feature_names=features,
                   filled=True,
                   ax=axes[index],
                   proportion=True)

    axes[index].set_title('Train Estimator: ' + str(index))
fig.savefig('train_trees.png')

test_random_forest = RandomForestClassifier(n_estimators=5)
test_random_forest = test_random_forest.fit(x_test, y_test)

fig, axes = plt.subplots(nrows=1, ncols=test_random_forest.n_estimators, figsize=(20, 4), dpi=900)
for index in range(0, test_random_forest.n_estimators):
    tree.plot_tree(test_random_forest.estimators_[index],
                   feature_names=features,
                   filled=True,
                   ax=axes[index],
                   proportion=True)

    axes[index].set_title('Test Estimator: ' + str(index))
fig.savefig('test_trees.png')