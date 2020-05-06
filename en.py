#!/bin/python3

import urllib.parse, base64, sys

# Coded By Abdul
# Trying my best to keep the code simple.
# this tool does URL and base64 encoding and decoding.
# Usage:
#	- urlencoding:
#		python3 en.py
#
# 		type whatever text to urlencode it  or you can simply do :
#
#		echo "TEXT" | python3 en.py
#
#	- base64 encoding :
#
#               python3 en.py
#
#               before starting the actaul text to encode type "b64 " at the begining of the string. or you can simply do :
#
#               echo "b64 TEXT" | python3 en.py

# Decoding
#		add the option '-d'  :
#		python3 en.py -d
#
#		same procedure as encoding , no need to explain more.

decode = False

if len(sys.argv) >1 and sys.argv[1] == "-d":
		decode=True

while True:
	output=""
	try:
		text = input().strip()

		# check if Base64
		if(text.startswith("b64 ")):
			if decode == True:
				try:
					output = base64.b64decode(text[4:]) .decode('ascii')

				except (base64.binascii.Error,UnicodeDecodeError) as e:
					print("\n",e)
			else:
				output = base64.b64encode(text[4:].encode('ascii')).decode('ascii')
		else:
			if decode==True:
				output = urllib.parse.unquote(text)
			else:
				output = urllib.parse.quote(text)

		print("\n"+output)
		print("-"*30+"\n")

	except (KeyboardInterrupt,EOFError):
		break
