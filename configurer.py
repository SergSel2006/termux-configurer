#!/bin/python

import subprocess

import time

adv=False
subprocess.run("clear", shell=True)
print("welcome to the second stage!")
print("here is two ways of configuring your termux:")
print("")
print("1: Basic installisation")
print("    automatically install and/or updating all packages that are commonly used")
print("")
print("2: advanced installisation")
print("    do everything as in basic installisation and let you choose what instaall additional")
print("")
print("type X for exit")
print("")
print("")
inp=input("what way you will use?[1/2]:")
if inp == "1":
	subprocess.run("clear")
	print("you choosed basic installisation")
	print("the automaic istallisation will start after 5 seconds")
	time.sleep(6)
elif inp == "2":
	adv=True
	subprocess.run("clear")
	print("you choosed advanced installisation")
	print("programm will ask you some questions")
	time.sleep(5)
	subprocess.run("clear")
elif inp == "x" or inp == "X":
	exit("Bye")
else:
	exit("Please, reastart and select 1 or 2")
if adv == True:
	mpd=input("Would you like to install music player?[Y/N]")
	if mpd == "y" or mpd == "Y":
		mpd="1"
		print("run mpd and then ncmpcpp to use music player")
		time.sleep(3)
	else:
		mpd="0"
	subprocess.run("clear")
	ssh=input("will you use ssh?[Y/N]")
	if ssh == "y" or ssh == "Y":
		ssh="1"
		print("run sshd to start ssh server, pkill sshd to kill it")
		time.sleep(3)
	else:
		ssh="0"
	subprocess.run("clear")
	repos=input("would you like to install unstable and X11 repositories?[Y/N]")
	if repos == "y" or repos == "Y":
		repos="1"
		print("repositories will be installed")
		time.sleep(3)
	else:
		repos="0"
subprocess.run("clear")
subprocess.run("pkg update && pkg install nano ruby pkg-config mc zsh man texinfo bash-completion wget", shell=True)
if adv == True:
	if mpd == "1":
		subprocess.run("pkg install mpd ncmpcpp", shell=True)
	elif ssh == "1":
		subprocess.run("pkg install openssh", shell=True)
	elif repos == "1":
		subprocess.run("pkg install unstable-repo x11-repo", shell=True)
subprocess.run("alias aliases_config_bash='nano ~/.bashrc' && alias aliases_config_zsh='nano ~/.zshrc'", shell=True)
exit("Second stage finished! you can run aliases_config_[your shell] to configure aliases. syntax: alias (alias name)='coomand'")
