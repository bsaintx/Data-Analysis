import pandas as pd
table = pd.read_excel("Vendas.xlsx")

#  Overview of total billing
total_billing = table["Valor Final"].sum()
print(total_billing)
