import matplotlib.pyplot as plt
import pandas
from sklearn import linear_model

from sklearn.model_selection import train_test_split

df = pandas.read_json("../data/data.json")

d = {'Rock': 0, 'Pop': 1, 'Pop Rock': 2, 'Alternative Rock':3, 'Flamenco':4, 'Electronic':5}
df['gender'] = df['gender'].map(d)

features = ['year']

x = df[features]
y = df['gender']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

logistic = linear_model.LogisticRegression()
linear = logistic.fit(x_train, y_train)

z_pred = logistic.predict_proba(x_test)

score = logistic.score(x_test, y_test)
print("Acuracy: \n",score)

plt.scatter(x_test, y_test, color="black")
plt.plot(x_test, z_pred, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()