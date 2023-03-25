#!/usr/bin/python3 

from pwn import *
import re

context.log_level = "critical"a
host = "213.177.18.70"
port = 9999
s = remote(host,port)

# receive info from server
text = s.recv().decode()
#print(text)

# send answer
s.sendline(b"martie")

# get response and trim out the flag
response = s.recvline().decode()
flag = response.split(" ")[5]

print(flag)

# close connection
s.close()
