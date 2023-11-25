import pandas
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

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

knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(x_train, y_train)

classes = x_test.gender

new_x = x_test.likes[0]
new_y = x_test.gender[0]
new_point = [(new_x, new_y)]

prediction = knn.predict(new_point)

plt.scatter(x_test.likes, x_test.gender, c=classes)
plt.scatter(x_test.likes + [new_x], y_test + [new_y], c=classes + [prediction[0]])
plt.text(x=new_x - 1.7, y=new_y - 0.7, s=f"new point, class: {prediction[0]}")
plt.show()
