# smartscan_registration_module.py

# In-Memory Storage: Simulate a database using a list of dictionaries
user_records = []

# Lambda function to create a new user record
create_user = lambda name, email: {'name': name, 'email': email}

# Lambda function to insert the user record into the list
insert_user = lambda user: user_records.append(user)

# Lambda function to fetch all user records from the list
fetch_all_users = lambda: user_records

# Function to decode the SmartScan Code without using base64 module
def decode_smartscan_code(encoded_data):
    # A simple manual decode function assuming the input is a simple transformation for the example
    # Here we reverse the string twice for demonstration purposes
    decoded_data = encoded_data[::-1]  # Simulate a simple encoding/decoding process
    decoded_data = decoded_data[::-1]
    return decoded_data

# User Registration Function
def RegisterUserFromSmartScan(encoded_data):
    # Decode the SmartScan Code to extract user data
    user_data = decode_smartscan_code(encoded_data)
    
    # Extract name and email from the decoded data
    name, email = user_data.split(',')
    
    # Create a new user record using the lambda function
    new_user = create_user(name, email)
    
    # Insert the user record into the in-memory list
    insert_user(new_user)
    
    # Print the list of all registered users
    for user in fetch_all_users():
        print(f"Name: {user['name']}, Email: {user['email']}")
