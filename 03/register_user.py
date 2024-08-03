# register_user.py

import smartscan_registration_module as srm

# Example SmartScan Code (manually encoded)
# Let's assume the SmartScan code contains "John Doe,john.doe@example.com"
# For this example, we manually reverse the string twice to simulate encoding
user_data = "John Doe,john.doe@example.com"
encoded_smartscan_code = user_data[::-1][::-1]

# Register the user using the SmartScan code
srm.RegisterUserFromSmartScan(encoded_smartscan_code)
