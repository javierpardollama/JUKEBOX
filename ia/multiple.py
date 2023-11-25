import matplotlib.pyplot as plt
import pandas
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import numpy as np

df = pandas.read_json("../data/data.json")

df = df.dropna()

db = {False: 0, True: 1}
df['bought'] = df['bought'].map(db)
dg = {'Rock': 0, 'Pop': 1, 'Pop Rock': 2, 'Alternative Rock': 3, 'Flamenco': 4, 'Electronic': 5}
df['gender'] = df['gender'].map(dg)

features = ['likes', 'gender']

x = df[features]
y = df['bought']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

linear = linear_model.LinearRegression()
linear = linear.fit(x_train, y_train)

z_pred = linear.predict(x_test)

print("Coefficients: \n", linear.coef_)
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(y_test, z_pred))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(y_test, z_pred))


x_line = np.linspace(x_test.likes.min(), x_test.likes.max(), 100)
y_line = np.linspace(x_test.gender.min(), x_test.gender.max(), 100)
z_vals = linear.predict(np.concatenate((x_line.reshape(-1, 1), y_line.reshape(-1, 1)), axis=1))

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x_test.likes, x_test.gender, y_test)
ax.plot(x_line, y_line, z_vals)

ax.set(title="Multiple Regression with SciKit Learn", xlabel='likes', ylabel='gender', zlabel='bought')

plt.show()
