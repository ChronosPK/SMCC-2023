## Solve

Unzip, make executable, run, run `strings` on it and `grep` for the flag.

```bash
┌──(chronos㉿hackmachine)-[~/CTFs/AFT/prep/linux3]
└─$ unzip verify.zip     
Archive:  verify.zip
  inflating: verify                  
                                                                                                                                                                                             
┌──(chronos㉿hackmachine)-[~/CTFs/AFT/prep/linux3]
└─$ ls
verify  verify.zip
                                                                                                                                                                                             
┌──(chronos㉿hackmachine)-[~/CTFs/AFT/prep/linux3]
└─$ chmod +x verify       
                                                                                                                                                                                             
┌──(chronos㉿hackmachine)-[~/CTFs/AFT/prep/linux3]
└─$ ./verify     
What is the flag?: as
Input is not correct, try again
What is the flag?: c
Input is not correct, try again
What is the flag?: ^C
                                                                                                                                                                                             
┌──(chronos㉿hackmachine)-[~/CTFs/AFT/prep/linux3]
└─$ strings verify | grep -i flag   
What is the flag?: 
flaggg
flag
                                                                                                                                                                                             
┌──(chronos㉿hackmachine)-[~/CTFs/AFT/prep/linux3]
└─$ ./verify 
What is the flag?: flaggg
Input is correct!
```

<br>

## Flag:
`flaggg`
