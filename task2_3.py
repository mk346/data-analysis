#task 2 part 3 binarizing columns with yes or no to 1 and 0

# import python library
import pandas as pd

# reading the csv file to use
task2_3 = pd.read_csv("task2_2.csv")

# binarizing columns with yes and no values to 1 and 0
task2_3.Churn.replace(('Yes', 'No'), (1, 0), inplace=True)
task2_3.PhoneService.replace(('Yes', 'No'), (1, 0), inplace=True)
task2_3.OnlineSecurity.replace(('Yes','No','No internet service'), (1,0,0), inplace=True)
task2_3.OnlineBackup.replace(('Yes','No','No internet service'), (1,0,0), inplace=True)
task2_3.DeviceProtection.replace(('Yes','No','No internet service'), (1,0,0), inplace=True)
task2_3.StreamingTV.replace(('Yes','No','No internet service'), (1,0,0), inplace=True)
task2_3.StreamingMovies.replace(('Yes','No','No internet service'), (1,0,0), inplace=True)
task2_3.PaperlessBilling.replace(('Yes','No','No internet service'), (1,0, 0), inplace=True)
task2_3.MultipleLines.replace(('Yes', 'No', 'No phone service'), (1, 0, 0), inplace=True)

#print the first 5 rows
print(task2_3.head(5))

# writing the new data frame to csv file
task2_3.to_csv("task2_3.csv")
