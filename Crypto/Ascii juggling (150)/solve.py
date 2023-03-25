#!/usr/bin/python3

import re

h = open("encoded.txt")
c = h.read()
h.close()

decoded = ''.join([chr(int(dec)) for dec in c.split()])

print(''.join(re.findall('flag{.*}',decoded)))
