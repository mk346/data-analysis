# task 2 part 2 => Remove all rows with Null values/ empty attribute values

#import the necessary python libraries
import pandas as pd

# reading the csv file to use
task2_2 = pd.read_csv("task2_1.csv")

# dropping null rows using dropna function
task2_2.dropna()

# saving the new dataframe to a csv file
task2_2.to_csv("task2_2.csv")