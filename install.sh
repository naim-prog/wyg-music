#!/bin/bash

if [ $(id -u) != '0' ]
then
	echo "Run this script with sudo so you don't have any problems"
	exit 1
fi


sudo apt install redis

# pip install -r requirements.txt
