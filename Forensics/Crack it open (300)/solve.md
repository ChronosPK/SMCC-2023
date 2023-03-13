## References from intro:
Answer to the riddle: `Handshake`. <br>

<br>

## Analyze the packet capture
In the packet capture, we can see many `802.11` packets, which means we are dealing WI-FI. <br>
If we need to look for a handshake ([4-way handshake](https://www.wifi-professionals.com/2019/01/4-way-handshake)). <br>
We can filter in Wireshark for packets involved in a handshake: `eapol`.

<br>

## What now?
Now that we identified the problem, we need an explication. <br>
What happened here? 

<br>

I tried to deauthenticate a client from his router and capture his handshake upon automatic reconnection. <br>
You can see some `deauthentication` packets in the pcap file. <br>
I also presented this attack in my introductory course: https://chronossec.site/network_attacks.

<br>

## Crack the password
Just use `aircrack-ng` with `rockyou.txt` as wordlist to crack the Wi-Fi password. <br>

```bash
aircrack-ng crack-it-open.cap -w /usr/share/wordlists/rockyou.txt
```

<br><br>

## Flag
`flag{hatehackers}`
