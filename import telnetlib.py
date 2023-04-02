import telnetlib

# Define the login credentials and device information
HOST = "192.168.1.1"
user = "admin"
password = "password"

# Connect to the network device
tn = telnetlib.Telnet(HOST)

# Enter the login credentials
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")

# Send the commands to create VLAN 10
tn.write(b"conf t\n")
tn.write(b"vlan 10\n")
tn.write(b"name VLAN10\n")
tn.write(b"exit\n")
tn.write(b"exit\n")

# Verify that VLAN 10 has been created
tn.write(b"show vlan\n")
output = tn.read_until(b"Total").decode('ascii')
print(output)

# Close the connection
tn.close()