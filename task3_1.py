# task 3 part 1 => Multiple lines and churn; the relationship between telecommunication company’s customers having multiple lines and churning
# in this case i will use linear regression to visualize the relationship

# importing the necessary libraries
import pandas as pd
from sklearn.linear_model import LinearRegression

# reading the training and testing dataset csv files
training = pd.read_csv("training.csv")
testing = pd.read_csv("testing.csv")
test_label = pd.read_csv("test_label.csv")

X_train = training[['MultipleLines']] 
y_train = training[['Churn']]
X_test = testing[['MultipleLines']]

# training the model
regressor = LinearRegression(fit_intercept=True)
regressor.fit(X_train, y_train)

# print the slope 
print('Slope of the Line (m)', regressor.coef_) # note the slope is positive hence MultipleLines and Customer Churning are directly propotioanal 

# print the gradient
print('Gradient of the line (x)', regressor.intercept_)