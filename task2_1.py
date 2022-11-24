# task 2 part 1 => dropping irrelevant columns in customerchurn csv file

#import the necessary python libraries
import pandas as pd;

#reading the customer churn csv file
customer_churn = pd.read_csv("Customer_Churn.csv");


# dropping the irrelevant columns
customer_churn.drop(['customerID','Partner','Dependents','TechSupport','Contract'], axis = 1, inplace = True)
print(customer_churn.head(5)) # outputs the first 5 records

# save the new dataframe to a csv file
customer_churn.to_csv("task2_1.csv")