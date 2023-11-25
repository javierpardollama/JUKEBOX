import matplotlib.pyplot as plt
import numpy as np
import pandas
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from scipy.special import expit


df = pandas.read_json("../data/data.json")

df = df.dropna()

d = {False: 0, True: 1}
df['bought'] = df['bought'].map(d)

features = ['likes']
x = df[features].to_numpy()
y = df['bought'].to_numpy()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

logis = linear_model.LogisticRegression()
logis.fit(x_train, y_train)

x_line = np.linspace(x_test.min(), x_test.max(), x_test.size)

plt.scatter(x_test.ravel(),y_test)
loss = expit(x_line * logis.coef_ + logis.intercept_).ravel()
plt.plot(x_line, loss, label="Logistic Regression Model", color="red", linewidth=3)

plt.xlabel('likes')
plt.ylabel('bought')

plt.show()

