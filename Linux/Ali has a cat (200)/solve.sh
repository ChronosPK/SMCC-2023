#!/bin/bash

# Check if sshpass is installed
if ! command -v sshpass &> /dev/null
then
    echo "sshpass is not installed. Installing it now..."
    sudo apt-get install sshpass -y
fi

# SSH parameters
user="user"
host="213.177.18.70"
port="5000"
password="userpass"

# Command to execute
command="cat flag.txt"

# Connect to remote server via SSH and execute command
sshpass -p "${password}" ssh -o StrictHostKeyChecking=no -p "${port}" "${user}@${host}" "${command}"

# unalias is bypassed if you run the command in a separate shell terminal
