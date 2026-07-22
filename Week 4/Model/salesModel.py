# Using Linear regression to predict sales

# importing libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# importing cleaned dataset
df = pd.read_csv('week4\capstone_cleaned.csv')

# feature selection
features = [
    'Product',
    'Country',
    'Segment',
    'Discount Band',
    'Units Sold',
    'Manufacturing Price',
    'Sale Price',
    'Discounts',
    'COGS'
]
# not using profit because sales - cost = profit
X = df[features]
y = df['Sales']

# encoding
categorical = [
    'Country',
    'Product',
    'Segment',
    'Discount Band'
]
numeric = [
    'Units Sold',
    'Manufacturing Price',
    'Sale Price',
    'Discounts',
    'COGS'
]

preprocessor = ColumnTransformer(
    transformers = [
        ('cat', OneHotEncoder(handle_unknown = 'ignore'), categorical),
        ('num', 'passthrough', numeric)
    ]
)

# pipeline
model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

# training
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# model train
model.fit(x_train, y_train)

# prediction
y_pred = model.predict(x_test)

# evaluation
print("R² Score:", r2_score(y_test, y_pred))
'''
R² Score: 0.9962547701380294
meaning that model explains 99.63% of the variance in sales
predicted sales are very close to actual sales
excellent fit for the model
'''
print("MAE:", mean_absolute_error(y_test, y_pred))
'''
MAE: 9536.974074319976
on avg model is off by 9536.97 in predicting sales
considering the scale of our sales (over 1 million), this is a very small error
'''
print("RMSE:", mean_squared_error(y_test, y_pred) ** 0.5)
'''
RMSE: 14402.170500381095
on avg model is off by 14402.17 in predicting sales
rmse is higher than mae because it penalizes larger errors more than smaller ones
rmse of 14k is still low
'''

# Actual vs Predicted
plt.figure(figsize=(7,6))
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    color="red"
)
plt.show()
# most points are close to the red line
# indicating that the model is predicting sales accurately