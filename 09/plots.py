import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('employee_performance.csv')

# Display the first few rows of the dataset
print(data.head())

# Set up the matplotlib figure
plt.figure(figsize=(12, 8))

# 1. Histogram
plt.subplot(3, 3, 1)
plt.hist(data['Years_of_Experience'], bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Frequency')

# 2. Scatter Plot
plt.subplot(3, 3, 2)
plt.scatter(data['Years_of_Experience'], data['Client_Satisfaction_Rating'], color='purple')
plt.title('Scatter Plot: Experience vs. Satisfaction')
plt.xlabel('Years of Experience')
plt.ylabel('Client Satisfaction Rating')

# 3. Line Plot
plt.subplot(3, 3, 3)
data['Average_Satisfaction'] = data.groupby('Department')['Client_Satisfaction_Rating'].transform('mean')
plt.plot(data['Department'], data['Average_Satisfaction'], marker='o', linestyle='-', color='green')
plt.title('Line Plot: Avg Satisfaction by Department')
plt.xlabel('Department')
plt.ylabel('Average Client Satisfaction Rating')
plt.xticks(rotation=45)

# 4. Bar Graph
plt.subplot(3, 3, 4)
data['Department'].value_counts().plot(kind='bar', color='orange')
plt.title('Bar Graph: Number of Employees by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')

# 5. Pie Chart
plt.subplot(3, 3, 5)
data['Department'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title('Pie Chart: Proportion of Employees by Department')
plt.ylabel('')  # Hide y-label

# 6. Area Plot
plt.subplot(3, 3, 6)
data.groupby('Department')['Projects_Completed'].sum().plot(kind='area', alpha=0.5)
plt.title('Area Plot: Total Projects Completed by Department')
plt.xlabel('Department')
plt.ylabel('Total Projects Completed')

# 7. Box Plot
plt.subplot(3, 3, 7)
sns.boxplot(x='Department', y='Client_Satisfaction_Rating', data=data)
plt.title('Box Plot: Satisfaction Ratings by Department')
plt.xlabel('Department')
plt.ylabel('Client Satisfaction Rating')

# 8. Pair Plot
plt.figure(figsize=(10, 6))
sns.pairplot(data[['Years_of_Experience', 'Projects_Completed', 'Client_Satisfaction_Rating']])
plt.suptitle('Pair Plot: Relationships Among Variables', y=1.02)

# Show all plots
plt.tight_layout()
plt.show()
