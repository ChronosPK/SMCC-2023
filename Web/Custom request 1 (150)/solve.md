## Solve:


## Connect
```bash
curl 206.189.59.199:8007/first
```
```plain
Complete the following tasks to get the flag: 
    Supply a query in your URL containing the following:
        - the name of the application used to build the server
        - the version of that application 
    Send the query in the "flag" sub-directory.
```
<br><br>


## Check the server's application by requesting `-v` verbose output 
```bash
curl 213.177.18.70:8007/first -v
```
```plaintext
< Server: BaseHTTP/0.6 Python/3.7.16
```
<br/><br/>


## Supply the python version as parameter
```bash
curl 213.177.18.70:8007/first/flag?python=3.7.16
```
```plain
flag{cf4d66370a137b574b4c7e548ff56983b828b457dcbaaf177f0b4797972bc16f}
```
<br><br>

## Flag:

`flag{cf4d66370a137b574b4c7e548ff56983b828b457dcbaaf177f0b4797972bc16f}`
