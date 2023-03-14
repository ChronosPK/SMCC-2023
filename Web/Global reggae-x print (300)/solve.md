## Solve:
- [ ] **`Mirror`** the site (download every file as in a local mirror) and **`grep`** the flag recursively 

  ```bash
  wget -m http://213.177.18.70:8001
  grep --no-filename -RioP "flag{.*?}" .
  ```
<br>

## Flag:
`flag{grep_w1ll_d0_7h3_j0b}`
