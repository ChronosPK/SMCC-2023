## Solve:
1. We have a `jpg` file, so we try `stegseek`
```bash
stegseek spot-me.jpg                                                           
[i] Found passphrase: "!!!7056334111???"  
[i] Original filename: "mountians_and_sh8t.zip".
[i] Extracting to "spot-me.jpg.out".
```
<br>

2. Many blank lines, so we try `stegsnow`
```bash
stegsnow -C spot-me.jpg.out
ZmxhZ3s3aDE1X3c0eV8zNDV5XzQ1XzRfNW4wd2ZsNGszfQ== 
```
<br>

3. decode `base64`                                                                                                                  
```bash
echo 'ZmxhZ3s3aDE1X3c0eV8zNDV5XzQ1XzRfNW4wd2ZsNGszfQ==' | base64 -d
flag{7h15_w4y_345y_45_4_5n0wfl4k3}
```

<br>

## Flag:
`flag{7h15_w4y_345y_45_4_5n0wfl4k3}`
