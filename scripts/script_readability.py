#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Authors:
	Coraline MARIE

:Date:
	2014/12/3
"""

import sys
import os
import codecs
import glob


if __name__ == "__main__":

    for file_html in glob.glob("/home/coraline/Documents/Corpus/readability/corpus/el/html/*"):
        # file_tmp = open(file_html, "r")
        print(file_html.split("/")[-1])
        tmp = os.system("/home/coraline/Documents/Corpus/readability/python-readability/readability/readability.py -u "#
         + file_html + " > " + "/home/coraline/Documents/Corpus/readability/result/el/" + file_html.split("/")[-1])

    for file_html in glob.glob("/home/coraline/Documents/Corpus/readability/corpus/en/html/*"):
        # file_tmp = open(file_html, "r")
        print(file_html.split("/")[-1])
        tmp = os.system("/home/coraline/Documents/Corpus/readability/python-readability/readability/readability.py -u "#
         + file_html + " > " + "/home/coraline/Documents/Corpus/readability/result/en/" + file_html.split("/")[-1])

    for file_html in glob.glob("/home/coraline/Documents/Corpus/readability/corpus/pl/html/*"):
        # file_tmp = open(file_html, "r")
        print(file_html.split("/")[-1])
        tmp = os.system("/home/coraline/Documents/Corpus/readability/python-readability/readability/readability.py -u "#
         + file_html + " > " + "/home/coraline/Documents/Corpus/readability/result/pl/" + file_html.split("/")[-1])

    for file_html in glob.glob("/home/coraline/Documents/Corpus/readability/corpus/ru/html/*"):
        # file_tmp = open(file_html, "r")
        print(file_html.split("/")[-1])
        tmp = os.system("/home/coraline/Documents/Corpus/readability/python-readability/readability/readability.py -u "#
         + file_html + " > " + "/home/coraline/Documents/Corpus/readability/result/ru/" + file_html.split("/")[-1])

    for file_html in glob.glob("/home/coraline/Documents/Corpus/readability/corpus/zh/html/*"):
        # file_tmp = open(file_html, "r")
        print(file_html.split("/")[-1])
        tmp = os.system("/home/coraline/Documents/Corpus/readability/python-readability/readability/readability.py -u "#
         + file_html + " > " + "/home/coraline/Documents/Corpus/readability/result/zh/" + file_html.split("/")[-1])