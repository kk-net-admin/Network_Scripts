import subprocess

#name = (input("Enter the name you want to look up "))

command = subprocess.run(["nslookup", "google.com"], capture_output=True, text=True)

data = command.stdout.split()

# Find where 'Name:' and 'Addresses:' start
try:
    name_index = data.index("Name:")
    addr_index = data.index("Addresses:")
    
    # Print the name (the item right after 'Name:')
    print(f"{data[name_index]} {data[name_index + 1]}")
    
    # Print 'Addresses:' and everything after it
    print(f"{data[addr_index]} " + ", ".join(data[addr_index + 1:]))

except ValueError:
    print("Could not find the expected information in the output.")







