## Unzio recursively - one of the files contains the flag   

- unzip to a temporary directory `temp`
- for loop checking every file available (`ls temp`)
   - unzip every zip archive inside
      - `grep` recursively the string `flag` and sort values (only diferent values)

<br>

```bash
unzip linux-1.zip -d temp
for i in `ls temp`; do unzip temp/$i -d temp ;done
{ grep -Ri flag temp | cut -d":" -f 2 | sort -u } 2>/dev/null
```

<br>

## Flag:
`flag{you_found_me}`
