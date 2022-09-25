import pandas as pd
table = pd.read_excel("sales.xlsx")

#  Overview of total billing
total_billing = table["Valor Final"].sum()

# 
