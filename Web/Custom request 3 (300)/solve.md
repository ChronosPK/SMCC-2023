## Solve:
We are given an elf binary (linux interpreted). <br>
We make it executable and look for ports that have been opened in result of execuing it. <br>
Make a request on localhost on the specified port ad follow the instructions. <br>
Bruteforce the password in the query. <br>
Follow redirects with `curl` and get the flag.

<br>

- Check file properties, make it executable and run it
  ```bash
  chronos@hackmachine:~/CTFs/AFT/web/custom-req/third$ file server3
  third: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=ef678cfba147a70daf198e097736e386ccf2118b, for GNU/Linux 3.2.0, stripped
  
  chronos@hackmachine:~/CTFs/AFT/web/custom-req/third$ chmod +x server3
  
  chronos@hackmachine:~/CTFs/AFT/web/custom-req/third$ ./server3
  ```

<br>

- Check local network (use another terminal, don't close the program)
  ```bash
  netstat -tunlp
  
  tcp        0      0 0.0.0.0:5050            0.0.0.0:*               LISTEN      5730/./server3
  ```

<br>

- Now that we know the port that the application is listening on, we check it out using `curl`
  ```bash
  curl 127.1:5050
  
  This is the root directory.
  Provide a query in which you bruteforce a password.
  The parameter is "password".
  
  BTW, can you follow redirects more than 1000 times?
  ```
- You will also see the request being made on the tab hosting the program
  

<br>

- Create the URL query, select the wordlist (rockyou.txt) and loop through the wordlist
  ```bash
  while read -r line; do echo $line; curl -s 127.1:5050?password=$line; done < /usr/share/wordlists/rockyou.txt | grep -B2 redirect
  ```
  - echo the current line we are requesting
  - while loop to read `line` by `line` from the input file " < /usr/share/wordlists/rockyou.txt "
  - request page silently `-s`
  - find in all that output the sequence starting 2 lines before `-B2` the searched word "redirect"
  
  We found the password
  ```
  celtic
  Good query! Now redirect to lt4v2txdp9gn11yr
  ```

<br>

- Follow the redirect, but the intro says more than 1000 times (`curl`'s default is 50 redirects)
  ```bash
  curl 127.1:5050?password=celtic -L --max-redirs 1000
  ```
  ```
  Congrats, here you go: flag{redirect_redirect_go_ahead}
  ```

<br>

## Flag:

`flag{redirect_redirect_go_ahead}`
