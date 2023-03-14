## Crack the zip password 
```bash
zip2john zipfile.zip > hash.txt
john --format=zip hash.txt
```

## Cracking linux password hashes
```bash
unshadow passwd shadow > unshadowed
john --format=crypt --wordlists=/usr/share/wordlists/rockyou.txt unshadowed
```
If you won't use `format=crypt`, john won't recognize it. <br>
You can see the type from the `/etc/shadow` file - the character(s) between the `$` is **`y`**: `flag:$y$j9T$K9qxxEWOD2/tza...` 

<br>

## Flag:
`flag{iloveyou20}`
