import os
import pandas as pd
print "Hello"


# Getting present working directory
pwd = os.getcwd()

# Reading csv file
df = pd.read_csv(pwd + '/data.csv')

# Filtering dataframe
df_payments = df[df.id_client > 100]
df_payments = df_payments[df_payments.id_cliente % 20 == 0]
df_payments = df_payments[['id_cliente', 'revenue']]
