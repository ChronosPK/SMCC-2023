## Rewind 
Context from intro: <br>
`He said it is not valid and that I should help him find the secret signature`.

<br>

## What is it?
Search the given string online (or the title) and you will find out it is a JWT (JSON Web Token).

<br>

## What to do with it?
Search online for signature and secrets in JWT tokens. <br>
You will come across the idea of **cracking the weak secret**.

<br>

## Now what?
Github has your sollution most of the times. <br>
Check out the available tools, go with [this one](https://github.com/hahwul/jwt-hack).

<br>

## Get the flag
```bash
/jwt-hack crack 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4iLCJwYXNzIjoiU3VwZXJzZWNyZXRwYXNzd29yZG5vb25ld2lsbGZpZ3VyZWl0b3V0IiwiaWF0IjoxNTE2MjM5MDIyfQ.Z1HcZqsFYASj4P-XSub0mRc1i5YO9Cx5j4pB3xLbn2w' -w /usr/share/wordlists/rockyou.txt
   d8p 8d8   d88 888888888          888  888 ,8b.     doooooo 888  ,dP 
   88p 888,o.d88    '88d     ______ 88888888 88'8o    d88     888o8P'  
   88P 888P`Y8b8   '888      XXXXXX 88P  888 88PPY8.  d88     888 Y8L 
88888' 88P   YP8 '88p               88P  888 8b   `Y' d888888 888  `8p
-------------------------
[*] Start dict cracking mode
INFO[0010] Loaded words (remove duplicated)              size=14344384
INFO[0038] Found! Token signature secret is jwtswat      Signature=Verified Word=jwtswat
[+] Found! JWT signature secret: jwtswat
[+] Finish crack mode
```

<br><br>

## Flag:
`flag{jwtswat}`
