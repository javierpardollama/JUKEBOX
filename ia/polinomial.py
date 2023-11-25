import matplotlib.pyplot as plt
import numpy as np
import pandas
from sklearn.metrics import r2_score

df = pandas.read_json("../data/data.json")

df = df.dropna()

d = {False: 0, True: 1}
df['bought'] = df['bought'].map(d)

x = df['likes'].to_numpy()
y = df['bought'].to_numpy()

model1 = np.poly1d(np.polyfit(x, y, 1))
model3 = np.poly1d(np.polyfit(x, y, 3))
model7 = np.poly1d(np.polyfit(x, y, 7))

x_line = np.linspace(x.min(), x.max(), 100)

print("R² (x):  ", r2_score(y, model1(x)))
print("R² (x³): ", r2_score(y, model3(x)))
print("R² (x⁷): ", r2_score(y, model7(x)))

plt.subplot(2, 3, 2)
plt.scatter(x, y)
plt.plot(x_line, model1(x_line), label="1st degree (x)")
plt.plot(x_line, model3(x_line), label="3rd degree (x³)")
plt.plot(x_line, model7(x_line), label="7th degree (x⁷)")
plt.legend(loc="lower right")
plt.title("Polinomial regression with NumPy")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.subplot(2, 3, 4)
plt.scatter(x, y)
plt.plot(x_line, model1(x_line))
plt.title("1st degree (Linear Regression)")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.subplot(2, 3, 5)
plt.scatter(x, y)
plt.plot(x_line, model3(x_line))
plt.title("3rd degree")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.subplot(2, 3, 6)
plt.scatter(x, y)
plt.plot(x_line, model7(x_line))
plt.title("7th degree")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.show()