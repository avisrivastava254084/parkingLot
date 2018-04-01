#!/bin/bash

echo Hello, welcome to LeagueSX Parking lot!
echo Please select one of the options!
echo 1. Create Slot\(s\)
echo 2. Generate a ticket 
echo 3. Vacate a Slot
echo 4. Data Analysis
var1="1"
var2="2"
var3="3"
var4="4"
read option
if [ $option = $var1 ]
then
	python createNewSlot.py
fi

if [ $option = $var2 ] 
then
	python tickets.py
fi

if [ $option = $var3 ] 
then
	python vacate.py
fi

if [ $option = $var4 ]
then
	python data.py
fi

if [ $option != $var1 -a $option != $var2 -a $option != $var3 -a $option != $var4 ]
then
	echo Wrong option selected!
fi
