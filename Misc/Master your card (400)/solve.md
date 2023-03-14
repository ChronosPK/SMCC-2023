## Solve:

With the link provided, analyze the algorithm used in card numbers. <br>
The number has a specification for "BENDIGO" - category of cards from which we can look up the first few digits. <br>

<br>

The final script we will use to see the possible variants is the following:
```python
#!/usr/bin/python3

import re
import string

digits = string.digits

skelet = "5192446X41X95X20"

number = [a for a in skelet[::]]
#print(number)
# unknown values: 7, 10, 13

# go through all possible values for each 'X' 
possible = []
valid=[]
for i in range(10):
	for j in range(10):
		for k in range(10):
			number[7] = i
			number[10] = j
			number[13] = k
			number = [int(n) for n in number]
			possible.append(number)

#print(possible[::])
#print()

## start the validation algorithm
for i in possible[::]:
	aux = "".join(str(v) for v in i)
	# double digits on odd positions
	# 1 2 3 4 5 6 7 8 9 
	# 2 2 6 4 10 6 14 8 18
	for n in range(len(i))[::2]:
		i[n] *= 2 
		
		#print(odd)
		# if the result is greater than 10, substract 9 from it
		# 2 2 6 4 1 6 5 8 9
		if i[n] >= 10:
			i[n] -= 9

	# add all digits, if the sum is sivisible by 10, the card is valid
	if not sum(i[::]) % 10:
		valid.append(aux)
	
print(''.join(["flag{" + i +"}\n" for i in valid]))
```

<br>

 Take out the 90th variant from the output and you will get the final flag.

<br>

## Flag:
`flag{5192446841995220}`
