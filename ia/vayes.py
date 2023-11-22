import pandas
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
)
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

df = pandas.read_json("../data/data.json")

d = {'Rock': 0, 'Pop': 1, 'Pop Rock': 2, 'Alternative Rock':3, 'Flamenco':4, 'Electronic':5}
df['gender'] = df['gender'].map(d)

features = ['year', 'gender']

x = df[features]
y = df['gender']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

vayesian = GaussianNB()
vayesian.fit(x_train, y_train)

y_pred = vayesian.predict(x_test)

print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print('accuracy is', accuracy_score(y_pred, y_test))