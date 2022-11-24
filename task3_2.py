# task 3 part 2 => Total charges versus churn; the relationship between total charges to customers and churn

# using linear regression to visualize the relationship

# importing the necessary libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# reading the training and testing dataset csv files
training = pd.read_csv("training.csv")
testing = pd.read_csv("testing.csv")
test_label = pd.read_csv("test_label.csv")

#converting the totalcharges column from object dtype to float
training["TotalCharges"] = pd.to_numeric(training["TotalCharges"], errors='coerce')

# dropping the NaN values in the dataset
training_data= training.dropna(axis= 0, how='any')

# assigning x_train and y_train 
X_train = training_data[['TotalCharges']]
y_train = training_data[['Churn']]



# training the model
regressor = LinearRegression(fit_intercept=True)
regressor.fit(X_train, y_train)

# print the slope 
print('Slope of the Line (m)', regressor.coef_) # note the slope is negative hence totalcharges and churn have an inverse relationship

# print the gradient
print('Gradient of the line (x)', regressor.intercept_)