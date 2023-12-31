import matplotlib.pyplot as plt
import pandas
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

df = pandas.read_json("../data/data.json")

df = df.dropna()

d = {False: 0, True: 1}
df['bought'] = df['bought'].map(d)

features = ['likes']

x = df[features]
y = df['bought']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

linear = linear_model.LinearRegression()
linear = linear.fit(x_train, y_train)

z_vals = linear.predict(x_test)

print("Coefficients: \n", linear.coef_)
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(y_test, z_vals))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(y_test, z_vals))

plt.scatter(x_test, y_test, color="black")
plt.plot(x_test, z_vals, color="blue", linewidth=3)

plt.xlabel('likes')
plt.ylabel('bought')

plt.show()
