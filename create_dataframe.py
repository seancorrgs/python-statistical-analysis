import pandas as pd

# read data from csv file into a pandas dataframe
# WARNING: The string below is the path to the file on my local machine.  
# You should change it to the path to the file on your own machine.
preg = pd.read_csv('C:\code\python\FemPreg.csv')

# print row and column size of dataframe to verify
# should print: (13593, 244)
print(preg.shape)

