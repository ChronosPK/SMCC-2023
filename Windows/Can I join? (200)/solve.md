### Add user `CTF` to the machine and in the Administrators group. Password is `CTF`. 
The command should look like this: <br>
`net user ... && ...`

<br>

## Flag:
```cmd
net user CTF CTF /add && net localgroup Administrators CTF /add

net user /add CTF CTF && net localgroup Administrators CTF /add

net user CTF CTF /add && net localgroup /add Administrators CTF 

net user /add CTF CTF && net localgroup /add Administrators CTF
```
