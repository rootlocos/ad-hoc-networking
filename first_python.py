#!/usr/bin/env python3.9

#test output display
print("Python file is open...")

import paramiko

# Define the parameters for SFTP connection
host = "192.168.2.2" # Replace with IP address of the other Raspberry Pi
port = 22
username = "pi" # Replace with the username for the other Raspberry Pi
password = "Aa123456" # Replace with the password for the other Raspberry Pi

# Create an SFTP client object
transport = paramiko.Transport((host, port))
transport.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

# Transfer a file from the current Raspberry Pi to the other Raspberry Pi
local_file_path = "home/pi/Hello_File.txt" # Replace with the path to the local file
remote_file_path = "/home/alon/Desktop/pi/Receiving_Files/Hello_File_R.py" # Replace with the path to the remote file on the other Raspberry Pi
sftp.put(local_file_path, remote_file_path)

# Transfer a file from the other Raspberry Pi to the current Raspberry Pi
remote_file_path = "/home/alon/Desktop/pi/Sending_Files/Hello_File.py" # Replace with the path to the remote file on the other Raspberry Pi
local_file_path = "home/pi/Receiving_Files/Hello_File_R.py" # Replace with the path to the local file
sftp.get(remote_file_path, local_file_path)

# Close the SFTP client and transport
sftp.close()
transport.close()

#test output display
print("Python file is close...")
