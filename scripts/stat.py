#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Authors:
	Carl Goubeau

:Date:
	2014/12/08 (creation)
	2014/12/27 (last update)
"""

import sys
import os
import codecs
import glob
import math
from subprocess import call



#TODO normalize results/authors according to the number of patterns



def usage():
	"""
	display how to use the script
	"""
	print "usage: python " + sys.argv[0].split("/")[-1] + " [FILE_DIR]"



def get_stat(f):
	p = os.popen("grep '<p>' " + f + " | wc -l").read()[:-1]
	l = os.popen("cat " + f + " | wc -l").read()[:-1]
	w = os.popen("cat " + f + " | wc -w").read()[:-1]
	c = os.popen("cat " + f + " | wc -c").read()[:-1]

	return [p, l, w, c]



def main():
	if not len(sys.argv) > 1:
		print "[ERROR] "+sys.argv[0]+" expected at least 1 argument !"
		usage()
		sys.exit(2)

	patterns_dir = sys.argv[1]
	if not os.path.isdir(patterns_dir):
		print "[ERROR] "+sys.argv[0]+": " + patterns_dir + " is not a directory !"
		usage()
		sys.exit(2)

	file_dir = sys.argv[1]

	stat = [0, 0, 0, 0]
	nb = 0

	for f in glob.glob(file_dir + "/*"):
		r = get_stat(f)
		stat[0] += int(r[0])
		stat[1] += int(r[1])
		stat[2] += int(r[2])
		stat[3] += int(r[3])
		nb += 1

	print "<p>\t", stat[0]
	print "lines\t", stat[1]
	print "words\t", stat[2]
	print "chars\t", stat[3]
	print "nb_fi\t", nb


if __name__ == "__main__":
	main()

