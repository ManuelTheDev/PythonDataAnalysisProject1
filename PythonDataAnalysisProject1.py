import os
import pandas as pd
print "Hello"


# Getting present working directory
pwd = os.getcwd()

# Reading csv file
df = pd.read_csv(pwd + '/data.csv')
