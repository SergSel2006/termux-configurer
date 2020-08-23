#!/bin/sh

echo "Hi, tis is termux-configurer first stage!"
echo "installing dependences:"
apt-get install python pyton2
echo "first stage finished! Going to second stage"
python $PWD/configurer.py
