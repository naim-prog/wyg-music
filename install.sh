#!/bin/bash

if [ $(id -u) != '0' ]
then
	echo "Run this script with sudo so you don't have any problems"
	exit 1
fi

# Install redis
sudo apt install redis

# Install python packages
pip install -r requirements.txt
