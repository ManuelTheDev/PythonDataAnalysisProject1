print "Hello"

import pandas as pd
import os

#Getting present working directory
pwd = os.getcwd()

#Reading csv file
df = pd.read_csv(pwd + '/data.csv')