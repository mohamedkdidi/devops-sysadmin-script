#!/usr/bin/env python
# Author: mohamedkdidi@gmail.com 
# Get ip address of any website using socket.


# Import the necessary packages!
import socket as socket 

# Get my local hostname
my_hostname = socket.gethostname()

# Display my hostname
print('Your hostname is: ' + my_hostname)

# Get my local ip adress
my_ip = socket.gethostbyname(my_hostname)

# Display my ip 
print('Your ip address is: ' + my_ip)

# Input the domain name 
host = input('Enter the domain name, example (python.org): ')

# Fetch the ip
ip = socket.gethostbyname(host)

# Display the ip
print('The ip address of ' + host + ' is: '  + ip)