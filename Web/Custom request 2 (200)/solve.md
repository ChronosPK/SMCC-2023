## Solve:


## Connect
```bash
curl 206.189.59.199:8008/second
```
```plain
Complete the following tasks to get the flag:
    Create the query containing param. "flag" and value "please".
    Send the query in the "flag" sub-directory.
    Provide the "Sibiu-Academic-CTF" header with the MD5 hash of "winner" as the header value.
```

<br><br>

## Request the necessary query inside `/flag` directory
```bash
curl 206.189.59.199:8008/second/flag?flag=please
```
```plain
Check your Header.
```

<br><br>


## Determine the MD5 hash of "winner"
```bash
echo -n "winner" | md5sum
```
```plain
978f6f608df5279d4d85e700d83ac873  -
```

<br><br>

## Supply everything together as requested
```bash
curl 206.189.59.199:8008/second/flag?flag=please -H "Sibiu-Academic-CTF: 978f6f608df5279d4d85e700d83ac873"
```
```plain
flag{055f8f6aaae4bd63bbc44c81278b9c0afa17c2d7cdf8d39e5649e34d09770407}
```

<br><br>

## Flag:

`flag{055f8f6aaae4bd63bbc44c81278b9c0afa17c2d7cdf8d39e5649e34d09770407}`

