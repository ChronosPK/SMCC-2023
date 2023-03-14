## Calculate the original checksum
```bash
sha256sum order.json 
2c34b68669427d15f76a1c06ab941e3e6038dacdfb9209455c87519a3ef2c660  order.json
```
<br>

## Mmodify the "amount" from 1000 to 9000
```bash
cat order.json 
{
  "sender": "Alice",
  "recipient": "Mallory",
  "currency": "USD",
  "amount": 9000,
  "notes": "weekly payment"
}
```
<br>

## Check the new checksum
```bash
sha256sum order.json
11faeec5edc2a2bad82ab116bbe4df0f4bc6edd96adac7150bb4e6364a238466  order.json
```
<br>

## Calculate the xor of the 2 hex strings (hashes) 
[You can use this site.](https://xor.pw/)

<br><br>

## Flag:
`flag{3dce58438480dfaf2f40ad101070c1312bfe37149148ce505733b7ac74d14206}`
