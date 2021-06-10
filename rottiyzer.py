#!/usr/bin/env python3
from string import ascii_uppercase as upper
from string import ascii_lowercase as lower
import argparse
import sys

def parse_args():
    # parse the arguments
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython3 ' + sys.argv[0] + " -o 2 -m tzou")
    parser.add_argument('-o', '--mode', help="Type 1 for all attempts or Type 2 For useful only", type=int)
    parser.add_argument('-m', '--message', help='Type the Rotated Text', required=True)
    return parser.parse_args()

words = ['flag', 'FLAG', 'CTF', 'Flag', 'answer','FlAg']
#This is 1337 Line Banner for copyright
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

def btats(o,m):
	print("[*] Simple script to Bruteforce The Rotation Number")
	message = m
	choose = int(o)
	if int(choose) == int(1) or choose =="":
		print("[*] Well you chose the hard way")
		for n in range(1,26):
			print([n],rot(message,n=n))
	elif choose == int(2):
		print("[*] No Output? Try the first option")
		for n in range(1,26):
			for theuseful in words:
				checking = rot(message,n=n)
				if theuseful in checking:
					print([n],checking)
	else:
		print("[-] Invaild Option")

def interactive():
    args = parse_args()
    o = args.mode
    m = args.message
    if not o:
    	o = 1
    calling = btats(o,m)


if __name__ == "__main__":
    interactive()

