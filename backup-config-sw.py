#!/usr/bin/python
import sys
import time
import paramiko 
import os
import cmd
import datetime

# Credentials
USER = 'admin'
PASSWORD = '1234'

# Array with the IP of the switches and their respective names
SWITCHES = [ 
    ['192.168.1.10', 'SW-SALES'],
    ['192.168.1.11', 'SW-HR'],
    ['192.168.1.12', 'SW-ACCOUNTING'],
    ['192.168.1.13', 'SW-IT'],
    ['192.168.1.14', 'SW-PUBLIC'],
    ['192.168.1.15', 'SW-PARK'],
]

# Define the initial value of the counter
i = 0

# Goes over the loaded switches
while i < len(SWITCHES):
    # Start the SSH session
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(SWITCHES[i][0], username = USER, password = PASSWORD)

    # Open the console
    chan = client.invoke_shell()
    time.sleep(1)

    # Execute commands in console
    chan.send('term len 0\n')
    time.sleep(1)
    chan.send('sh run\n')
    time.sleep(5)

    # Take what is written on the console and decodes it to UTF-8
    output = chan.recv(99999)
    output = output.decode('utf-8')

    # Take the current date and time
    now = datetime.datetime.now()

    # Creates the file with the network device's name plus the actual time on its name, and writes the current configuration on it
    filename = "%s_%.2i-%.2i-%i_%.2i-%.2i-%.2i.txt" % (SWITCHES[i][1], now.day, now.month, now.year, now.hour, now.minute, now.second)
    f = open("/home/backups-folder/switches/" + filename, 'w+')
    f.write(output)
    f.close()

    # Closes the SSH session
    client.close()

    # Increase the counter value
    i = i + 1
