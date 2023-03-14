## Hint:

- [ ] Set of blacklisted characters (not allowed) <br>
  <sup>```blacklist = ["~","!","@","#","$","%","^","&","*","(",")","_","-","+","{","}","]","[","|","\\","|",";",",",".","<",">","?","/","`",":","\""]```</sup>

<br>

- [ ] If the characters introduced are not in the blacklist, the command given is **normalized** <br>
  ```norm = unicodedata.normalize("NFKC", cmd)```

<br>

- [ ] We can request regular commands, but in order to get the flag we need to bypass the blacklist. <br>
    We do this by using special characters in **Unicode** that are the equivalent of normal characters after **normalization**. <br>
    We see some examples here: https://lazarv.com/posts/unicode-normalization-vulnerabilities/
