import pickle
import base64

# Example data to be encoded
data = {'role': 'Staff', 'username': 'test'}

# Serialize the data using pickle
serialized_data = pickle.dumps(data)

# Base64 encode the serialized data
encoded_data = base64.b64encode(serialized_data).decode()

# Create the cookie string
cookie_name = "session"
cookie_value = f".{encoded_data}."
cookie = f"{cookie_name}{cookie_value}"

# Print the encoded cookie string
print(cookie)