import matplotlib.pyplot as plt
import pandas
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

df = pandas.read_json("../data/data.json")

d = {'Rock': 0, 'Pop': 1, 'Pop Rock': 2, 'Alternative Rock':3, 'Flamenco':4, 'Electronic':5}
df['gender'] = df['gender'].map(d)

features = ['year']

x = df[features]
y = df['gender']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

kneighbours = KNeighborsClassifier(n_neighbors=3)

kneighbours.fit(x_train, y_train)

z_pred = kneighbours.predict_proba(x_test)

plt.scatter(x_test, y_test, color="black")
plt.plot(x_test, z_pred)

plt.xlabel('year')
plt.ylabel('gender')

plt.show()
