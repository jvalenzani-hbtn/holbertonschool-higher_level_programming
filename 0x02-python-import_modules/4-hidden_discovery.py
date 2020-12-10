#!/usr/bin/python3

import hidden_4

for a in dir(hidden_4):
	if a[0:2] != "__":
		print("{}".format(a))
