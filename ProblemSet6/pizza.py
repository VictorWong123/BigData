from tabulate import tabulate
import pandas as pd

table =[]
with open('sicilian.csv') as file:
    for line in file:
        table.append([line])

print(tabulate(table,tablefmt='grid'))





df = pd.read_csv('sicilian.csv')

print(tabulate(df,tablefmt='grid'))



