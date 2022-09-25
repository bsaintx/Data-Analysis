import pandas as pd
table = pd.read_excel("sales.xlsx")

#   Overview of total sales
total_sales = table["Final Price"].sum()

#   Company Sales - Top -> Down
company_sales = table[["Company", "Final Price"]].groupby("Company").sum()

# Top selling products
top_selling = table[["Company", "Final Price"]].groupby(["Company", "Product"]).sum()
