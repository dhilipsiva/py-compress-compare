import json

# Define the size target in bytes
target_size = 1 * 1024 * 1024  # 1 MB

# Create a sample data entry
data = {
    'name': 'John Doe',
    'age': 30,
    'email': 'johndoe@example.com',
    'address': '1234 Elm Street, Anytown, USA'
}

# Convert the data entry to a JSON string to estimate size
sample_entry = json.dumps(data)
entry_size = len(sample_entry.encode('utf-8'))

# Calculate how many such entries are needed to reach approximately 1 MB
num_entries = target_size // entry_size

# Generate the list of entries
json_data = [data for _ in range(num_entries)]

# Write the JSON data to a file
with open('sample_data.json', 'w') as file:
    json.dump(json_data, file)

print(f"Generated file 'sample_data.json' with approximately 1 MB of JSON data.")
