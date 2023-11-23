import matplotlib.pyplot as plt
import pandas
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

df = pandas.read_json("../data/data.json")

d = {'Rock': 0, 'Pop': 1, 'Pop Rock': 2, 'Alternative Rock':3, 'Flamenco':4, 'Electronic':5}
df['gender'] = df['gender'].map(d)

df = df[df['year'].notnull()]
df = df[df['year'].notna()]

features = ['year']

x = df[features]
y = df['gender']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

linear = linear_model.LinearRegression()
linear = linear.fit(x_train, y_train)

z_pred = linear.predict(x_test)

print("Coefficients: \n", linear.coef_)
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(y_test, z_pred))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(y_test, z_pred))

plt.scatter(x_test, y_test, color="black")
plt.plot(x_test, z_pred, color="blue", linewidth=3)

plt.xlabel('year')
plt.ylabel('gender')

plt.show()