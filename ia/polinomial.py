import matplotlib.pyplot as plt
import pandas
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

df = pandas.read_json("../data/data.json")

df = df.dropna()

d = { False: 0, True: 1}
df['bought'] = df['bought'].map(d)

features = ['likes','gender']

x = df[features]
y = df['bought']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)