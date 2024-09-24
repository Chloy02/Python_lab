import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Sample data generation
num_employees = 100
data = {
    'Employee ID': np.arange(1, num_employees + 1),
    'Department': np.random.choice(['Engineering', 'HR', 'Marketing', 'Sales', 'Finance', 'IT'], size=num_employees),
    'Years of Experience': np.round(np.random.uniform(0, 15, size=num_employees), 1),
    'Projects Completed': np.random.randint(1, 21, size=num_employees),
    'Client Satisfaction Rating': np.round(np.random.uniform(1.0, 5.0, size=num_employees), 1)
}

# Create DataFrame
df = pd.DataFrame(data)

# Rename columns to replace spaces with underscores
df.columns = df.columns.str.replace(' ', '_')

# Save to CSV
df.to_csv('employee_performance.csv', index=False)

print("CSV file 'employee_performance.csv' created with sample employee data.")
