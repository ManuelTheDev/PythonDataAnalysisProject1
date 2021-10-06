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

# Defining variable
tax = 1.25

# Defining function to calculate tax


def calculate_tax(num):
    return num * tax


# Creating new dataframe grouping by a new column
df_payments_grouped = df_payments.copy()
df_payments_grouped = df_payments_grouped.groupby('id_client', as_index=False)
df_payments_grouped = df_payments_grouped['revenue'].mean()


# Saving data in a new csv
df_payments_grouped.to_csv(pwd + '/data_grouped.csv', index=False)
