
import sys
import time
import pyperclip
import getpass
import pyperclip as clipboard

import argparse
from argparse import RawTextHelpFormatter


def convertStringToMD5(plainPasswd):

	from hashlib import md5
	
	return md5(plainPasswd).hexdigest()
	
def convertStringToSHA256(plainPasswd):

	from hashlib import sha256
	
	return sha256(plainPasswd).hexdigest()
	
def convertStringToSHA512(plainPasswd):

	from hashlib import sha512
	
	return sha512(plainPasswd).hexdigest()
	
def convertPasswdToHash(plainPasswd, algorithm):
	
	algorithms = { "md5": convertStringToMD5, "sha256": convertStringToSHA256, "sha512": convertStringToSHA512 }
	
	return algorithms.get(algorithm)(plainPasswd)
	
def isAlgorithmCorrect(algorithm):

	return algorithm in [ "md5", "sha256", "sha512" ]
	
def timeBeforeClearingClipboard(TIMEOUT):

	time.sleep(TIMEOUT)

	clipboard.copy('')

if __name__ == "__main__":
	
	TIMEOUT = 5
	passwd = None

	parser = argparse.ArgumentParser()
	parser.formatter_class = RawTextHelpFormatter
	parser.description = 'CoverMyFuckingPasswd is a small script that converts your passwords into hashes.'
	parser.usage = "cmfp.py [OPTIONS]"
	parser.epilog = """\033[1;31mExample:\033[0;39m cmfp.py -h sha512 -t 10"""
	parser.add_argument('--hash', help='Convert to (md5, sha256, sha512) - Default: sha256 ', default="sha256")
	parser.add_argument('--timeout', '-t', help='Time the password will be on the clipboard', type=int, default=TIMEOUT)
	args = parser.parse_args()
	
	if not isAlgorithmCorrect(args.hash):
		print("[x] Algorithm not found")
		sys.exit(1)
	
	plainPasswd = getpass.getpass("[-] Password: ").encode()
	
	convertedPasswd = convertPasswdToHash(plainPasswd, args.hash)
	
	clipboard.copy(convertedPasswd)
	
	print("[+] Exported password \n[*] You have 5 seconds to use it.")
	
	timeBeforeClearingClipboard(args.timeout)
	
	print("[+] Password removed")

