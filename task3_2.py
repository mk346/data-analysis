# task 3 part 2 => Total charges versus churn; the relationship between total charges to customers and churn

# using linear regression to visualize the relationship

# importing the necessary libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
import re

# reading the training and testing dataset csv files
training = pd.read_csv("training.csv")
training_data = pd.DataFrame(training)
training_data['TotalCharges'] = training_data['TotalCharges'].str.strip()
training_data2 = re.findall(r'\d+\.\d+', training_data)
print(training_data.dtypes)
# testing = pd.read_csv("testing.csv")
# test_label = pd.read_csv("test_label.csv")
#dataframe['quantity'] = dataframe['quantity'].astype(float)
#training_data["TotalCharges"] = training_data["TotalCharges"].astype(str).astype(float)
# training['TotalCharges'].strip(" ")

# X_train = training[['TotalCharges']]
# y_train = training[['Churn']]
# training.strip('')


# print(X_train.dtypes)

# training the model
# regressor = LinearRegression(fit_intercept=True)
# regressor.fit(X_train, y_train)

# # print the slope 
# print('Slope of the Line (m)', regressor.coef_)

# # print the gradient
# print('Gradient of the line (x)', regressor.intercept_)