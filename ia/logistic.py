import matplotlib.pyplot as plt
import pandas
from sklearn import linear_model

from sklearn.model_selection import train_test_split

df = pandas.read_json("../data/data.json")

df = df.dropna()

d = { False: 0, True: 1}
df['bought'] = df['bought'].map(d)

features = ['likes']

x = df[features]
y = df['bought']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=50)

logistic = linear_model.LogisticRegression()
logistic = logistic.fit(x_train, y_train)

z_pred = logistic.predict_proba(x_test)[:,1]

score = logistic.score(x_test, y_test)
print("Acuracy: \n",score)

plt.scatter(x_test, y_test, color="black")

plt.plot(x_test, z_pred, color='red')

plt.xlabel('likes')
plt.ylabel('bought')

plt.show()