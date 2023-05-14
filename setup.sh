#!/bin/bash

area="$PWD"

if [ "$UID" = "0" ]; then

    if [ -f "$area/requirements.txt" ]; then

        pip install -r $area/requirements.txt

        apt install nmap -y
        apt install dnsmap -y
        apt install dmitry -y
        apt install assetfinder -y
        apt install nikto -y

        echo ""
        echo "Installed Requirements From 'requirements.txt'"
        echo ""

        exit 1

    else

        echo ""
        echo "Error: Please Ensure 'requirements.txt' Is Accessable In $PWD"
        echo ""

        exit 2

else

    echo ""
    echo "Please Run This Script As UID = 0"
    echo ""

    exit 3

fi

exit 999