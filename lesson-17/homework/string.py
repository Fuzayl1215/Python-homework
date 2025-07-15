import pandas as pd
import numpy as np

# Homework 1

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# 1. Rename column names
df.rename(columns={"First Name": "first_name", "Age": "age"}, inplace=True)

# 2. Print the first 3 rows
print("First 3 rows:")
print(df.head(3))

# 3. Mean age
mean_age = df['age'].mean()
print("\nMean age:", mean_age)

# 4. Select and print 'first_name' and 'City'
print("\nFirst Name and City:")
print(df[['first_name', 'City']])

# 5. Add random salary column
np.random.seed(42)
df['Salary'] = np.random.randint(50000, 100000, size=len(df))
print("\nWith Salary:")
print(df)

# 6. Summary statistics
print("\nSummary Statistics:")
print(df.describe(include='all'))

# Homework 2

sales_data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
              'Sales': [5000, 6000, 7500, 8000],
              'Expenses': [3000, 3500, 4000, 4500]}
sales_and_expenses = pd.DataFrame(sales_data)

print("\nSales and Expenses Data:")
print(sales_and_expenses)

# 2. Maximum
print("\nMax Sales and Expenses:")
print(sales_and_expenses[['Sales', 'Expenses']].max())

# 3. Minimum
print("\nMin Sales and Expenses:")
print(sales_and_expenses[['Sales', 'Expenses']].min())

# 4. Average
print("\nAverage Sales and Expenses:")
print(sales_and_expenses[['Sales', 'Expenses']].mean())

# Homework 3

expenses_data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}
expenses = pd.DataFrame(expenses_data)
expenses.set_index('Category', inplace=True)

# Max expense
print("\nMax expense per category:")
print(expenses.max(axis=1))

# Min expense
print("\nMin expense per category:")
print(expenses.min(axis=1))

# Average expense
print("\nAverage expense per category:")
print(expenses.mean(axis=1))
