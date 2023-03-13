## First:
```bash
openssl aes-256-cbc -pbkdf2 -iter 10000 -d -in first.txt.openssl  -out first.txt
```

<br>

## Second:
```bash
gpg --output second.txt --decrypt second.txt.gpg
```

<br>

## Flag:
`flag{cryp70_d3cryp710n_w17h_5ymm37r1c_k3y5}`
