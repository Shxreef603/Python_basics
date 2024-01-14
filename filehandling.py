# Data to be written to the file
data_to_write = """This is a sample text file.
It contains multiple lines.
Each line demonstrates file handling in Python.
"""

# File creation and writing
file_name = 'sample_file.txt'

# Writing to the file
with open(file_name, 'w') as file:
    file.write(data_to_write)

print(f"Data has been written to {file_name}")


