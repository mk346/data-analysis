# task 2 part 4 => Split the binarized data into training set and test set in the ratio of 2:1


#import the necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# read the csv file to use
task2_4 = pd.read_csv("task2_3.csv")
#print(task2_4.head(5)) # print the first 5 records

# Assign the values of X and Y where X is the independent variable while Y is the dependent variable
Y = task2_4[['Churn']] # churn is the dependent variable

# Independent variables are more than one
X1 = task2_4[['MultipleLines']] # first independent variable
X2 = task2_4[['StreamingTV']] # second independent variable
X3 = task2_4[['StreamingMovies']] # third independent variable
X4 = task2_4[['MonthlyCharges']] # fourth independent variable
X5 = task2_4['TotalCharges'] # fifth independent variable
#print(X1.head(5))

# splitting data into training set and test set
# since we have more than one independent variables we shall split one by one that is X1_ to X5_
# X1_train to X5_train represents the train dataset while X1_test to X5_test represents the test dataset for the independent variables
# y1_train to y5_train represents the train dataset while y1_test to y5_test represents the test dataset for the dependent variable
# test size will be 2/3 that is 2/3 for train data and 1/3 for test data
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, Y, test_size = 1/3, random_state = 42 )
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, Y, test_size = 1/3, random_state = 42 )
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, Y, test_size = 1/3, random_state = 42 )
X4_train, X4_test, y4_train, y4_test = train_test_split(X4, Y, test_size = 1/3, random_state = 42 )
X5_train, X5_test, y5_train, y5_test = train_test_split(X5, Y, test_size = 1/3, random_state = 42 )
# print(X1_train.shape) # printing the data shape x_train and y_train should be the same dimension
# print(X1_test.shape)
# print(y1_train.shape)
# print(y1_test.shape)

# writing the training dataset to a csv file
# creating a dataframe to append train dataset to
train_data = pd.DataFrame(X1_train)
# appending the rest of the columns to the dataframe
train_data['StreamingTV'] = X2_train
train_data['StreamingMovies'] = X3_train
train_data['MonthlyCharges'] = X4_train
train_data['TotalCharges'] = X5_train
train_data['Churn'] = y1_train
# write the training dataset to a csv file
train_data.to_csv("training.csv")


# writing the testing dataset of the independent variable to a csv file
# creating a dataframe to append test dataset to
test_data = pd.DataFrame(X1_test)
# appending the rest of the columns
test_data['StreamingTV'] = X2_test 
test_data['StreamingMovies'] = X3_test
test_data['MonthlyCharges'] = X4_test
test_data['TotalCharges'] = X5_test
# writing the test_data dataframe to a csv file
test_data.to_csv("testing.csv")





# task 2 part 5 => for testing dataset separate the dependent variable from independent variables
test_data_dependent_variable = pd.DataFrame(y1_test)
# write the dependent variable test dataset to a csv file
test_data_dependent_variable.to_csv("test_label.csv")




# new_data = pd.read_csv("dependent_variable.csv")
# new_data['MultipleLines'] = X1
#new_data.drop(['MultipleLines'],axis=1,inplace=True)
# print(new_data.head(5))
# X1.to_csv("dependent_variable.csv")
# .drop(['customerID','Partner','Dependents','TechSupport','Contract'], axis = 1, inplace = True)