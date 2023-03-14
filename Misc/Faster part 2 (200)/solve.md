## Solve:

- Analyzing the code, we see a `base64` encoded string and a `zlib` encoding of it
<br>

- decode the base64 string and redirect the output to a file 
  ```bash
  echo "eJxdUE1vwjAMvftXGCZEOlXAxG1SuHDYAWlognsVUtNGtE2UuGVl2n9fKso07RDZen4fdp4myzb45ck0S9dzaZs17KRpGC7S+aGa2lnP6An20tOiVqzLBxg4UgogeW8WKmhjsspeyWsVCMJjkJvCcPj1Uk1ua7jJe7MYSnwFweEB6dIaTXD2tkbTuJZNTbZlHB3+QOnxXvdat95TDh8yAEuCTh4EJ+DkTtzEepW+rFZJAhcxfTMdYU3IJWFFzORxFnCW4+AYFtOZ6FIXqVp2zw7Y96+AW/knUri4lmM532xwno6gXCeA5iz2QqfbJIkajFnv8Qq8Wn+Z4LlSxVdumzlnrlJ9duqzuEHm24rC9zSKqQo0yo7W4knlKcZ0VIUyzSQy6FOTY/x3cJSMihB/fuD9AAd6nY8=" | base64 -d > mini.zlib
  ```
<br>

- uncompress the zlib encryption 
  ```bash
  zlib-flate -uncompress < mini.zlib > out
  ```
<br>

- get the flag out of the code  
  ```bash
  grep -o 'flag{.*}' out
  ```

<br>

## Flag:
`flag{don't_play_by_the_rules}`
