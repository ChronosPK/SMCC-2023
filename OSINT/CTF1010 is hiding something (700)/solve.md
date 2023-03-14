## Solve:

- [ ] Github repository for user: http://github.com/CTF1010 

- [ ] Repo name is a hash, decoded is `fotosinteza`

- [ ] Check commits
  - see a link for the challenge [https://drive.google.com/uc?export=download&id=1tQePz6rgTl9QWfgy2Uzviilk7Vyfo-pE](https://drive.google.com/uc?export=download&id=1tQePz6rgTl9QWfgy2Uzviilk7Vyfo-pE)
  - image is password protected
  - image is also **not** relevant for location 

- [ ] Check releases
  - a code in which the password `1234567891011121314151617181920` is verified
  - this is the password for the image from the google drive link
  - the image password can also be found using `stegseek`
    - `stegseek this-mausoleum-i-think.JPG`

- [ ] Extract a zip archive from the image
  ```bash
  steghide extract -sf this-mausoleum-i-think.JPG
  Enter passphrase: 1234567891011121314151617181920
  ```

- [ ] Zip archive is password protected using the repo name found earlier (`fotosinteza`)
  - zip password can be cracked using `fcrackzip` or `zip2john` since the password is in `rockyou.txt` wordlist
    ```bash
    fcrackzip -D -u -p /usr/share/wordlists/rockyou.txt bm90aGVyZS4K.zip
    
    PASSWORD FOUND!!!!: pw == fotosinteza
    ```
    or <br>
    
    ```bash
    zip2john bm90aGVyZS4K.zip > hash.txt
    john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
    fotosinteza      (bm90aGVyZS4K.zip/spooky-girl.png)     
    ```

- [ ] [Reverse image search](https://www.google.com/maps/place/Mausoleum+of+Baron+von+Schroeder/@53.6285858,10.0461783,7a,54.2y/data=!3m8!1e2!3m6!1sAF1QipPTgmw5t0DFi3j2MscyxO47648Uc-5gzKyEAwvk!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipPTgmw5t0DFi3j2MscyxO47648Uc-5gzKyEAwvk%3Dw203-h270-k-no!7i3024!8i4032!4m12!1m6!3m5!1s0x0:0x2e5dc28fb587dcdb!2sOSINT+Open+Source+Intelligence+Training!8m2!3d53.6387821!4d10.0150667!3m4!1s0x47b189a5116f19ad:0x1ee39d7f191e3d43!8m2!3d53.6285858!4d10.0461783)

<br><br>

## Flag:
`flag{Mausoleum_of_Baron_von_Schroeder}`
