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

    for file_html in glob.glob("/home/coraline/Documents/Corpus/CME_Project/corpus/source/el/html/*"):
        # file_tmp = open(file_html, "r")
        print(file_html.split("/")[-1])
        tmp = os.system("/home/coraline/Documents/Corpus/CME_Project/scripts/html_killer.py "#
         + file_html + " > " + "/home/coraline/Documents/Corpus/CME_Project/corpus/html_killer/el/" + file_html.split("/")[-1])
    for file_html in glob.glob("/home/coraline/Documents/Corpus/CME_Project/corpus/source/en/html/*"):
        # file_tmp = open(file_html, "r")
        print(file_html.split("/")[-1])
        tmp = os.system("/home/coraline/Documents/Corpus/CME_Project/scripts/html_killer.py "#
         + file_html + " > " + "/home/coraline/Documents/Corpus/CME_Project/corpus/html_killer/en/" + file_html.split("/")[-1])
    for file_html in glob.glob("/home/coraline/Documents/Corpus/CME_Project/corpus/source/pl/html/*"):
        # file_tmp = open(file_html, "r")
        print(file_html.split("/")[-1])
        tmp = os.system("/home/coraline/Documents/Corpus/CME_Project/scripts/html_killer.py "#
         + file_html + " > " + "/home/coraline/Documents/Corpus/CME_Project/corpus/html_killer/pl/" + file_html.split("/")[-1])
    for file_html in glob.glob("/home/coraline/Documents/Corpus/CME_Project/corpus/source/ru/html/*"):
        # file_tmp = open(file_html, "r")
        print(file_html.split("/")[-1])
        tmp = os.system("/home/coraline/Documents/Corpus/CME_Project/scripts/html_killer.py "#
         + file_html + " > " + "/home/coraline/Documents/Corpus/CME_Project/corpus/html_killer/ru/" + file_html.split("/")[-1])
    for file_html in glob.glob("/home/coraline/Documents/Corpus/CME_Project/corpus/source/zh/html/*"):
        # file_tmp = open(file_html, "r")
        print(file_html.split("/")[-1])
        tmp = os.system("/home/coraline/Documents/Corpus/CME_Project/scripts/html_killer.py "#
         + file_html + " > " + "/home/coraline/Documents/Corpus/CME_Project/corpus/html_killer/zh/" + file_html.split("/")[-1])

