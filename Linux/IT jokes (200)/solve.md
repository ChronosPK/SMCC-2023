## What could it be?
```plain
Nice sPI, am I right?

101.23.281.56
101.23.281.27
101.23.281.56
101.23.281.86
101.23.281.97
101.23.281.57
101.23.281.76
101.23.281.87
101.23.281.56
101.23.281.76
101.23.281.56
101.23.281.27
```

- `sPI` is IPs, but reversed - reverse the IPs (3rd octed has values greater that 255 anyway)
- all octets are the same, but the last one (which will become the first after reversing)
- operate with the lines containing IPs only (last 12)

<br>

```bash
tail -n 12 hey_boss | rev | cut -d'.' -f1
65
72
65
68
79
75
67
78
65
67
65
72
```


Replace newline with spaces and head to decoder online 
```bash
tail -n 12 hey_boss | rev | cut -d'.' -f1 | tr '\n' ' '
65 72 65 68 79 75 67 78 65 67 65 72
```

Decode hex values and start from the last line (reverse again the order of characters)

<br>

## Flag:
`flag{regexguyhere}`
