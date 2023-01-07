import paramiko

# open the ssh client
ssh_client = paramiko.SSHClient()
print(type(ssh_client))

# Skips ssh fingerprint authorization using paramiko
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Puts router information into dictionary
router = {"hostname": '192.168.56.103', 'port': '22', 'username': 'gns3', 'password': 'gns3'}

# Connects to router using ssh client
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

# Checks if connection was successful
print(f'Connecting to {router["hostname"]}...')
print(ssh_client.get_transport().is_active())

# Break line
print('#' * 50)

# Closes connection
print('closing connection...')
ssh_client.close()