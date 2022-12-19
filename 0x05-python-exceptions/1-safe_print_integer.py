#!/usr/bin/python3
def safe_print_integer(value):
	try:
		if value % 2 == 0 || value % 2 != 0:
			print("{:d}".format(value))
		return True
	except TypeError:
		return False
