## Solve:

- [ ] Reverse string (you see it seems like base64, but the "`=`" for padding are at the beginning)
  ```bash
  echo -en "==gC90TPRdlNG1UVEZTVFllSPNDR180VRpVTLNlWZhkRKBlQMpVWXRlWP9EV0kEW040T" | rev
  T040WEk0VE9PWlRXWVpMQlBKRkhZWlNLTVpRV081RDNPSllFVTZEVU1GNldRPT09Cg==
  ```

- [ ] Base64 decode
  ```bash
  echo -en "==gC90TPRdlNG1UVEZTVFllSPNDR180VRpVTLNlWZhkRKBlQMpVWXRlWP9EV0kEW040T" | rev | base64 -d
  ON4XI4TOOZTWYZLBPJFHYZSKMZQWO5D3OJYEU6DUMF6WQ===
  ```
 
- [ ] Base32 decode
  ```bash
  echo -en "==gC90TPRdlNG1UVEZTVFllSPNDR180VRpVTLNlWZhkRKBlQMpVWXRlWP9EV0kEW040T" | rev | base64 -d | base32 -d
  sytrnvgleazJ|fJfagt{rpJxta}h
  ```

- [ ] XOR (bruteforce online - key = 15(hex))
  ```flag{crypto_is_just_strange_math}```
  
