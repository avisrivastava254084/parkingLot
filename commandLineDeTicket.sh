#!/bin/bash
# Ask the user for their name
echo Hello, welcome to LeagueSX Parking lot!
echo Please select one of the options!
echo 1. Create Slot\(s\)
echo 2. Generate a ticket 
var1="1"
var2="2"
read option
if [ $option = $var1 ]
then
	python createNewSlot.py
fi

if [ $option = $var2 ] 
then
	python tickets.py
fi

if [ $option != $var1 -a $option != $var2 ]
then
	echo Wrong option selected!
fi
