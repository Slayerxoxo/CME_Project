#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Authors:
	Coraline MARIE

:Date:
	2015/1/4
"""

import sys
import os
import codecs
import glob
from boilerpipe.extract import Extractor

if __name__ == "__main__":

    print ("coucou")
    for file_html in glob.glob("/home/coraline/Documents/Corpus/boilerpipe/source/el/html/*"):
    	print(file_html.split("/")[-1])
    	file_input_name = "file:///" + file_html
    	extractor = Extractor(extractor='ArticleExtractor', url=file_input_name)
    	file_output_name = "/home/coraline/Documents/Corpus/boilerpipe/result/el/" + file_html.split("/")[-1]
    	fichier = codecs.open(file_output_name, "w", "utf-8")
    	extracted_text = extractor.getText()
    	fichier.write(extracted_text)
    	fichier.close()
    for file_html in glob.glob("/home/coraline/Documents/Corpus/boilerpipe/source/en/html/*"):
    	print(file_html.split("/")[-1])
    	file_input_name = "file:///" + file_html
    	extractor = Extractor(extractor='ArticleExtractor', url=file_input_name)
    	file_output_name = "/home/coraline/Documents/Corpus/boilerpipe/result/en/" + file_html.split("/")[-1]
    	fichier = codecs.open(file_output_name, "w", "utf-8")
    	extracted_text = extractor.getText()
    	fichier.write(extracted_text)
    	fichier.close()
    for file_html in glob.glob("/home/coraline/Documents/Corpus/boilerpipe/source/pl/html/*"):
    	print(file_html.split("/")[-1])
    	file_input_name = "file:///" + file_html
    	extractor = Extractor(extractor='ArticleExtractor', url=file_input_name)
    	file_output_name = "/home/coraline/Documents/Corpus/boilerpipe/result/pl/" + file_html.split("/")[-1]
    	fichier = codecs.open(file_output_name, "w", "utf-8")
    	extracted_text = extractor.getText()
    	fichier.write(extracted_text)
    	fichier.close()
    for file_html in glob.glob("/home/coraline/Documents/Corpus/boilerpipe/source/ru/html/*"):
    	print(file_html.split("/")[-1])
    	file_input_name = "file:///" + file_html
    	extractor = Extractor(extractor='ArticleExtractor', url=file_input_name)
    	file_output_name = "/home/coraline/Documents/Corpus/boilerpipe/result/ru/" + file_html.split("/")[-1]
    	fichier = codecs.open(file_output_name, "w", "utf-8")
    	extracted_text = extractor.getText()
    	fichier.write(extracted_text)
    	fichier.close()
    for file_html in glob.glob("/home/coraline/Documents/Corpus/boilerpipe/source/zh/html/*"):
    	print(file_html.split("/")[-1])
    	file_input_name = "file:///" + file_html
    	extractor = Extractor(extractor='ArticleExtractor', url=file_input_name)
    	file_output_name = "/home/coraline/Documents/Corpus/boilerpipe/result/zh/" + file_html.split("/")[-1]
    	fichier = codecs.open(file_output_name, "w", "utf-8")
    	extracted_text = extractor.getText()
    	fichier.write(extracted_text)
    	fichier.close()
