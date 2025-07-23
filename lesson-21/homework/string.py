import pandas as pd
import matplotlib.pyplot as plt

# DataFrame 1: Student Grades
grades = pd.DataFrame({
    'StudentID': [1, 2, 3, 4, 5],
    'Math': [88, 75, 93, 85, 88],
    'English': [78, 80, 85, 90, 92],
    'Science': [84, 70, 90, 86, 94]
})

# 1. Average grade
grades['Average'] = grades[['Math', 'English', 'Science']].mean(axis=1)

# 2. Highest average
top_student = grades.loc[grades['Average'].idxmax()]

# 3. Total column
grades['Total'] = grades[['Math', 'English', 'Science']].sum(axis=1)

# 4. Bar chart
subject_averages = grades[['Math', 'English', 'Science']].mean()
subject_averages.plot(kind='bar', title="Average Grade per Subject")
plt.ylabel("Average Score")
plt.tight_layout()
plt.show()



import pandas as pd
import matplotlib.pyplot as plt

# DataFrame 2: Sales Data
sales = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=7),
    'Product A': [200, 220, 210, 240, 250, 130, 120],
    'Product B': [150, 160, 170, 180, 170, 100, 50],
    'Product C': [100, 110, 115, 120, 120, 120, 142]
})

# 1. Total sales for each product
product_totals = sales.drop(columns='Date').sum()

# 2. Highest sales day
sales['TotalSales'] = sales[['Product A', 'Product B', 'Product C']].sum(axis=1)
best_day = sales.loc[sales['TotalSales'].idxmax()]

# 3. % change
percent_change = sales.drop(columns=['Date', 'TotalSales']).pct_change() * 100

# 4. Line chart
plt.figure(figsize=(10, 5))
for col in ['Product A', 'Product B', 'Product C']:
    plt.plot(sales['Date'], sales[col], label=col)
plt.title("Sales Trends")
plt.xlabel("Date")
plt.ylabel("Units Sold")
plt.legend()
plt.tight_layout()
plt.show()



import pandas as pd
import matplotlib.pyplot as plt

# DataFrame 3: Employee Info
employees = pd.DataFrame({
    'EmployeeID': [1, 2, 3, 4, 5, 6],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Department': ['HR', 'IT', 'HR', 'IT', 'Marketing', 'Finance'],
    'Salary': [60000, 75000, 72000, 80000, 68000, 69500],
    'Experience': [2, 5, 3, 8, 4, 6]
})

# 1. Avg salary by department
avg_salary = employees.groupby('Department')['Salary'].mean()

# 2. Most experienced
most_exp = employees.loc[employees['Experience'].idxmax()]

# 3. Salary Increase from min salary
min_salary = employees['Salary'].min()
employees['Salary Increase %'] = ((employees['Salary'] - min_salary) / min_salary) * 100

# 4. Department distribution
dept_counts = employees['Department'].value_counts()
dept_counts.plot(kind='bar', title="Employee Count per Department")
plt.ylabel("Count")
plt.tight_layout()
plt.show()



import pandas as pd
import matplotlib.pyplot as plt

# DataFrame 4: Customer Orders
orders = pd.DataFrame({
    'OrderID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'CustomerID': [101, 102, 101, 103, 104, 101, 102, 104, 105, 103],
    'Product': ['A', 'B', 'A', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
    'Quantity': [2, 1, 3, 2, 1, 4, 2, 1, 2, 1],
    'Price': [100, 150, 100, 200, 100, 150, 200, 100, 150, 200]
})

# 1. Total revenue
orders['Total'] = orders['Quantity'] * orders['Price']
total_revenue = orders['Total'].sum()

# 2. Most ordered product
most_ordered = orders.groupby('Product')['Quantity'].sum().idxmax()

# 3. Avg quantity
avg_quantity = orders['Quantity'].mean()

# 4. Pie chart
product_sales = orders.groupby('Product')['Total'].sum()
product_sales.plot(kind='pie', autopct='%1.1f%%', title="Sales by Product")
plt.ylabel("")
plt.tight_layout()
plt.show()
