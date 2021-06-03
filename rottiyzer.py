#!/usr/bin/env python3
from string import ascii_uppercase as upper
from string import ascii_lowercase as lower
words = ['flag', 'FLAG', 'CTF', 'Flag', 'answer','FlAg']
# This is 1337 Line Banner for copyright
def rot(s, n):
    upper_start = ord(upper[0])
    lower_start = ord(lower[0])
    out = ''
    for letter in s:
        if letter in upper:
            out += chr(upper_start + (ord(letter) - upper_start + n) % 26)
        elif letter in lower:
            out += chr(lower_start + (ord(letter) - lower_start + n) % 26)
        else:
            out += letter
    return(out)

def btats():
	print("[-] Simple script to Bruteforce The Rotation Number")
	message = input("[-] Paste your rotated text here: ")
	choose = input("[-] Type 1 to show all attempts or Type 2 to show only useful attempts: ")
	if choose == "1" or choose =="":
		print("[-] Well you chose the hard way")
		for n in range(1,26):
			print([n],rot(message,n=n))
	elif choose == "2":
		print("[-] No Output? Try the first option")
		for n in range(1,26):
			for theuseful in words:
				checking = rot(message,n=n)
				if theuseful in checking:
					print([n],checking)
	else:
		print("[-] Invaild Option")
btats()