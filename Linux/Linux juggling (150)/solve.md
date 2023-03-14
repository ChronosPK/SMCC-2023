## Use `grep` to extract and `wc` to count
```bash
grep -o '\b[A-Z][A-Za-z0-9_@/\-]*\b' text.txt | wc -l
```

If you count `WPA/WPA2` as a word - you get 61. If you don't, yo uget 64.

<br>

## Flag:
`flag{61}`
