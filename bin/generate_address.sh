#!/bin/sh
echo $(hciconfig | awk '/BD Address/ { print $3 }') > config/bluetooth_address
