import numpy as np

# Define the number of employees
num_employees = 20

# Define the departments
departments = ['Engineering', 'HR', 'Marketing', 'Sales', 'Finance']

# Create a structured array
employee_dtype = np.dtype([
    ('Employee_ID', 'i4'),  # Integer ID
    ('Department', 'U15'),   # String (up to 15 characters)
    ('Years_of_Experience', 'f4'),  # Float
    ('Projects_Completed', 'i4'),    # Integer
    ('Client_Satisfaction_Rating', 'f4')  # Float
])

# Generate random data
np.random.seed(42)  # For reproducibility

employee_data = np.zeros(num_employees, dtype=employee_dtype)

employee_data['Employee_ID'] = np.arange(1, num_employees + 1)
employee_data['Department'] = np.random.choice(departments, num_employees)
employee_data['Years_of_Experience'] = np.round(np.random.uniform(0, 15, num_employees), 2)
employee_data['Projects_Completed'] = np.random.randint(1, 21, num_employees)
employee_data['Client_Satisfaction_Rating'] = np.round(np.random.uniform(1.0, 5.0, num_employees), 2)

# Function to filter employees by department
def filter_by_department(data, department):
    return data[data['Department'] == department]

# Function to identify employee with highest client satisfaction rating
def highest_client_satisfaction(data):
    index = np.argmax(data['Client_Satisfaction_Rating'])
    return data[index]

# Function to calculate averages
def calculate_averages(data):
    avg_projects = np.mean(data['Projects_Completed'])
    avg_experience = np.mean(data['Years_of_Experience'])
    return avg_projects, avg_experience

# Function to identify employees with less than 2 years of experience
def less_than_two_years(data):
    return data[data['Years_of_Experience'] < 2]

# Output results
print("Employee Data:")
print(employee_data)

# Filtering by department (e.g., 'Engineering')
engineering_employees = filter_by_department(employee_data, 'Engineering')
print("\nEmployees in Engineering Department:")
print(engineering_employees)

# Highest client satisfaction rating
best_employee = highest_client_satisfaction(employee_data)
print("\nEmployee with Highest Client Satisfaction Rating:")
print(best_employee)

# Calculate averages
avg_projects, avg_experience = calculate_averages(employee_data)
print(f"\nAverage Projects Completed: {avg_projects}")
print(f"Average Years of Experience: {avg_experience}")

# Employees with less than 2 years of experience
inexperienced_employees = less_than_two_years(employee_data)
print("\nEmployees with Less than 2 Years of Experience:")
print(inexperienced_employees)
