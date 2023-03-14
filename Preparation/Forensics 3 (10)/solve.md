## Method 1
  
- [ ] Look at the bytes, see an extra "hahaha--" before a "PK" (file signature for zip archive) <br>
  `base64` encode the file <br>
  `base64` encode the first part "hahaha--" <br>
  <br>
  
  <br>
  
- [ ] Extract the first part from the hole chunk <br>
  `base64` decode the remaining part, then extract the flag. <br>
  <br>
  
  ```bash
  base64 didi.bin > base
  cat base
  aGFoYWhhLS0KUEsDBBQAAAAIAHBZllV6ggzIKwAAAC0AAAAIABwAZmxhZy50eHRVVAkAA1MtpGP4
  LaRjdXgLAAEE6AMAAAToAwAAS8tJTK9OyUzJjM/MKygtic8vBZGJeSnxJRmp8WlA2fjM4vjK/NKi
  4louAFBLAQIeAxQAAAAIAHBZllV6ggzIKwAAAC0AAAAIABgAAAAAAAEAAACkgQAAAABmbGFnLnR4
  dFVUBQADUy2kY3V4CwABBOgDAAAE6AMAAFBLBQYAAAAAAQABAE4AAABtAAAAAAA=
  
  echo "hahaha--" | base64                                                                      
  aGFoYWhhLS0K
  
  echo "UEsDBBQAAAAIAHBZllV6ggzIKwAAAC0AAAAIABwAZmxhZy50eHRVVAkAA1MtpGP4
  LaRjdXgLAAEE6AMAAAToAwAAS8tJTK9OyUzJjM/MKygtic8vBZGJeSnxJRmp8WlA2fjM4vjK/NKi
  4louAFBLAQIeAxQAAAAIAHBZllV6ggzIKwAAAC0AAAAIABgAAAAAAAEAAACkgQAAAABmbGFnLnR4
  dFVUBQADUy2kY3V4CwABBOgDAAAE6AMAAFBLBQYAAAAAAQABAE4AAABtAAAAAAA=" | base64 -d > out
  
  file out 
  out: Zip archive data, at least v2.0 to extract, compression method=deflate
  
  unzip out
  ```

<br><br>

## Method 2
  
- [ ] Use the byte-carving tool `dd` <br>
  Count the number of bytes required to cut. <br>
  ![xxd output](https://user-images.githubusercontent.com/93029180/209116640-ba20e2c5-61fc-4bf9-af54-abb255f44792.png)
  <br>
  <br>
- [ ] Start carving: <br>
  ```bash
  dd if=didi.bin of=out.zip ibs=1 skip=9
  ```

<br><br>

## Flag:
`flag{didi_input_ouput_and_the_flag_is_yours}`
  
  
