#!/usr/bin/python

import base64
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('command',type=str, nargs='?', help='Command to encode')
parser.add_argument("-s", "--stdin", action="store_true", default=False, help="Read from stdin")
args = parser.parse_args()

if args.stdin == True:
	command = unicode(sys.stdin.read())
elif args.command:
	command = unicode(args.command)
else:
	sys.exit(parser.print_help())

encoded_cmd = ''
for char in command:
	encoded_cmd += char + "\x00"

print base64.b64encode(encoded_cmd)
