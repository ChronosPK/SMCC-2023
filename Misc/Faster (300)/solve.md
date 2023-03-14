## What do I need to do?
```plain
Get the flag and win, but you got to be fast!
I know you are not that fast - you need to automate this.
```
Connect to `213.177.18.70 1337`

<br>

## I provided you with a body and main ideas for the solving script 

This will be the final version:
```python
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
```

<br>

## Flag:
`flag{nice_python(_skills)_bro}`
