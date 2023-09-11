from cmd import InformationGathering, utility
import os
import sys

os.system("clear")

try:
	utility.main(sys.argv[1])
except IndexError:
	print("Usage: main.py <youtube id>\n")
