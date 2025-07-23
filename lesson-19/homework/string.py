import pandas as pd

# Load sales data
df_sales = pd.read_csv("task/sales_data.csv")

# --- Task 1: Aggregates per Category ---
category_stats = df_sales.groupby("Category").agg(
    Total_Quantity_Sold=("Quantity", "sum"),
    Average_Price=("Price", "mean"),
    Max_Quantity_Transaction=("Quantity", "max")
).reset_index()
print("Category-wise Aggregates:")
print(category_stats)

# --- Task 2: Top-selling product in each category ---
top_products = df_sales.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()
top_products = top_products.sort_values(['Category', 'Quantity'], ascending=[True, False])
top_selling = top_products.groupby('Category').first().reset_index()
print("\nTop-selling product per category:")
print(top_selling)

# --- Task 3: Date with highest total sales (Quantity * Price) ---
df_sales['TotalSales'] = df_sales['Quantity'] * df_sales['Price']
sales_by_date = df_sales.groupby('Date')['TotalSales'].sum().reset_index()
max_sales_date = sales_by_date.sort_values('TotalSales', ascending=False).head(1)
print("\nDate with highest total sales:")
print(max_sales_date)

# Load customer order data
df_orders = pd.read_csv("task/customer_orders.csv")

# --- Task 1: Customers with ≥ 20 orders ---
order_counts = df_orders.groupby("CustomerID")['OrderID'].nunique().reset_index(name='OrderCount')
customers_20plus = order_counts[order_counts['OrderCount'] >= 20]
print("Customers with ≥ 20 orders:")
print(customers_20plus)

# --- Task 2: Customers with avg price per unit > $120 ---
avg_price_per_customer = df_orders.groupby("CustomerID")["Price"].mean().reset_index(name='AvgPrice')
high_spenders = avg_price_per_customer[avg_price_per_customer["AvgPrice"] > 120]
print("\nCustomers with avg price > $120:")
print(high_spenders)

# --- Task 3: Product total quantity and price; filter where quantity < 5 ---
product_summary = df_orders.groupby("Product").agg(
    Total_Quantity=("Quantity", "sum"),
    Total_Revenue=("Price", lambda x: (x * df_orders.loc[x.index, 'Quantity']).sum())
).reset_index()

filtered_products = product_summary[product_summary["Total_Quantity"] >= 5]
print("\nProducts with total quantity ≥ 5:")
print(filtered_products)

import sqlite3
import numpy as np

# --- Load salary bands ---
salary_bands = pd.read_excel("task/population salary analysis.xlsx")

# --- Read population data from SQLite ---
conn = sqlite3.connect("task/population.db")
df_population = pd.read_sql_query("SELECT * FROM population", conn)

# --- Map salaries to bands ---
def assign_band(salary):
    for _, row in salary_bands.iterrows():
        if row['MinSalary'] <= salary <= row['MaxSalary']:
            return row['SalaryBand']
    return 'Unknown'

df_population['SalaryBand'] = df_population['Salary'].apply(assign_band)

# --- Task 1: Measures per Salary Category ---
band_stats = df_population.groupby('SalaryBand').agg(
    Population_Percent=("Salary", lambda x: round(len(x) / len(df_population) * 100, 2)),
    Avg_Salary=("Salary", "mean"),
    Median_Salary=("Salary", "median"),
    Population_Count=("Salary", "count")
).reset_index()
print("Statistics per Salary Band:")
print(band_stats)

# --- Task 2: Measures per State & Salary Category ---
state_band_stats = df_population.groupby(['State', 'SalaryBand']).agg(
    Population_Percent=("Salary", lambda x: round(len(x) / len(df_population[df_population['State'] == x.name[0]]) * 100, 2)),
    Avg_Salary=("Salary", "mean"),
    Median_Salary=("Salary", "median"),
    Population_Count=("Salary", "count")
).reset_index()
print("\nStatistics per State and Salary Band:")
print(state_band_stats)

