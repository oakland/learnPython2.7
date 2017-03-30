#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = "jizq"

import sys

def test():
	if len(sys.argv) == 1:
		print "hello world"
		# print sys.argv[0] 
		# "usingModule.py"
	elif len(sys.argv) == 2:
		print "hello %s" % sys.argv[1]
	else:
		print "too many args"

if __name__ == '__main__':
	test()