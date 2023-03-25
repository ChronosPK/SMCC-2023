#!/usr/bin/python3

from pwn import *
import re

# connection info
context.log_level = "critical"
host = "213.177.18.70"
port = 1337
s = remote(host,port)

# receive info from server, decode from bytes
text = s.recv().decode()

# extract letter and number of repetitions
letter = re.findall('\".*?\"',text)
letter = ''.join(letter)[1]

number = int(text.split(" ")[5])

# prepare result to send back to server
result = letter * number

# send the result in bytes
s.sendline(result.encode())

# print the output, decoded
print(s.recvline().decode())

# close connection, good habbit
s.close()
