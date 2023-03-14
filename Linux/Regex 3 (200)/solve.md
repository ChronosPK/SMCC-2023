## How many words contain at least 2 characters
```bash
grep -oE "[A-Za-z0-9\`~\!@#$%^&*\|/?.>,<;:'\"=+_-]{2,}\b" text.txt | wc -l
655
```

Analyze the command step by step:
- use `-E` to specify the regex pattern, combined with `-o` to show just the match
- set of characters between `[` `]`
  - words contain letters, digits and special characters
  - for example, `200,000` is a single word
  - `WPA/WPA2` is a single word, kind of :/ (should have tried differend options anyway)
- pipe the result to `wc`

<br>

## Flag:
`flag{655}`
