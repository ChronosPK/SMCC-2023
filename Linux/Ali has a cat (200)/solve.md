## Connect to the machine from your linux terminal
Connect to the machine
```bash
ssh user@213.177.18.70 -p5000
```

Insert the password ( `userpass` )
```bash
user@213.177.18.70's password:
```

## Reference to `alias`
If you say the name of the challenge in your head, you heard something like "alias". <br>
If you didn't hear or didn't know about the command, you see that none of the common commands work. <br>


## Get the flag
Search for interesting things online and find nothing. <br>
Research further and see that `alias` has a list of commands I changed. <br>
```bash
user@linux-ali:~$ alias
alias cat='/bin/true'
alias egrep='/bin/true'
alias fgrep='/bin/true'
alias find='/bin/true'
alias grep='/bin/true'
alias l='ls -CF'
alias la='ls -A'
alias last='/bin/true'
alias less='/bin/true'
alias ll='ls -alF'
alias ls='ls --color=auto'
alias more='/bin/true'
alias nano='/bin/true'
alias python='/bin/true'
alias python2='/bin/true'
alias python3='/bin/true'
alias source='/bin/true'
alias vi='/bin/true'
alias vim='/bin/true'
alias w='/bin/true'
alias who='/bin/true'
```

<br>

You can either `unalias` a command, such as `cat`, or rewrite the alias for it.
```bash
user@linux-ali:~$ unalias cat
user@linux-ali:~$ cat flag.txt 
flag{who_let_the_cat_out?}
```

Another variant, as a script:
[solve.sh](./solve.sh)
