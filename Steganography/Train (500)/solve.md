## List files of archive (password protected)
List files inside the archive
```bash
unzip -l archive.zip
```

All files start with "`796F75`" one file is called "`images-10/X2FuZF9tZQo=`"
<br><br>

## Decode the name 
Decode the name of most popular files from hex (`796F75`) and the only odd one from base64 (`X2FuZF9tZQo=`). <br>
You will get "`you_and_me`", which is the archive password.
```bash
unzip -P 'you_and_me' archive.zip
```
<br>

## Scan QR codes and extract a letter from each one
Make two `one-liner`s to scan the qr codes, redirect to files, then <br>
extract from each file only the relevant portion and sort everything to get unique values only.

```bash
for i in {1..50}; do zbarimg images-$i/* > out-$i; done
for i in {1..50}; do cat out-$i| cut -d "." -f3 | tr -d "\n"; echo ; done | sort -u
```
<br><br>

## Flag:
`flag{awesome_thing_you_did}`
