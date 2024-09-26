import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv('sales_data_analysis.csv')

print("Sales Data Preview:")
print(sales_data.head())

total_revenue_by_category = sales_data.groupby('Product_Category')['Revenue'].sum()

plt.figure(figsize=(10, 6))
total_revenue_by_category.plot(kind='bar', color='skyblue')
plt.title('Total Revenue by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

total_units_sold_by_category = sales_data.groupby('Product_Category')['Units_Sold'].sum()

plt.figure(figsize=(8, 8))
total_units_sold_by_category.plot(kind='pie', autopct='%1.1f%%', colors=plt.cm.Paired.colors)
plt.title('Proportion of Total Units Sold by Product Category')
plt.ylabel('') 
plt.show()
