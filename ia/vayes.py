import pandas
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
)
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

df = pandas.read_json("../data/data.json")

df = df.dropna()

d = { False: 0, True: 1}
df['bought'] = df['bought'].map(d)

features = ['likes']

x = df[features]
y = df['bought']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=50)

vayesian = GaussianNB()
vayesian.fit(x_train, y_train)

y_pred = vayesian.predict(x_test)

print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print('accuracy is', accuracy_score(y_pred, y_test))