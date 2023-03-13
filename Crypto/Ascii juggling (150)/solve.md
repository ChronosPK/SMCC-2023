## What is it?
Check https://www.dcode.fr/cipher-identifier if you don't recognize it - **ASCII ciphertext**.

<br>

## Decode in pyhton
```python
#!/usr/bin/python3

import re

h = open("encoded.txt")
c = h.read()
h.close()

decoded = ''.join([chr(int(dec)) for dec in c.split()])

print(''.join(re.findall('flag{.*}',decoded)))
```

<br>

## Decode online
https://www.dcode.fr/ascii-code
<br>
![decode online](https://user-images.githubusercontent.com/93029180/224765146-96603b3b-7ea6-49d6-ba5d-00c64104aee7.png)

<br>

## Flag:
`flag{ascii_juggling}`
