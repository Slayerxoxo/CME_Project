#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Authors:
	Carl Goubeau, Marie-Charlotte Daureu and Coraline Marie

:Date:
	2014/11/19 (creation)
"""

import select
import sys
import os
import codecs
import re



def usage():
	# How to use the script
	print "usage: ./html_killer.py <HTML_FILE> [TXT_RESULT]?\n\n\t[TXT_RESULT]: true if result without html tags"


def main():
	if len(sys.argv) > 1:
		# file exist ?
		if not os.path.isfile(sys.argv[1]):
			raise SystemExit, "[ERROR] " + sys.argv[1] + ": file not found !"
	else:
		print "[ERROR] "+sys.argv[0]+" expected at least 1 argument !"
		usage()
		sys.exit(2)


	file_obj = codecs.open(sys.argv[1], "r", "utf-8")
	html = file_obj.read()
	html = html.encode("utf-8")

	html = html.split("<body>")[-1].split("</body>")[0]

	html = re.sub("\n", "",html)
	html = re.sub("<h1.*?>", "<h1>", html)
	if"<h1>" in html:
		html = "<h1>"+html.split("<h1>")[1]
	html = re.sub("<br.*?>", "</br>",html)
	html = re.sub("<script.*?>.*?<\/script.*?>", "",html)
	html = re.sub("<form.*?>.*?<\/form>", "",html)
	html = re.sub("<!--.*?-->", "",html)
	html = re.sub("<img .*?/>", "",html)
	html = re.sub("</?div.*?/?>", "",html)
	html = re.sub("</?span.*?/?>", "",html)

	# links
	html = re.sub("<a.*?>(.*?)</a>", "\g<1>", html)

	# lists
	html = re.sub("<li.*?>(.*?)</li>", "", html)

	# headers
	html = re.sub("<h[02-9].*?>(.*?)</h.>", "", html)
	html = re.sub("<h1>(.*?)</h1>", "<h>\g<1></h>", html)

	# p
	html = re.sub("<p.*?>", "<p>",html)
	html = re.sub("<p>(.*?)</p>", "<p>\g<1></p>", html)
	html = re.sub("<p>", "", html)
	html = re.sub("</p>", "</br>", html)
	html = re.sub("(</br>)+", "</br>", html)


	html = re.sub("<[^bph/].*?>.*?<\/[^ph].*?>", "",html)
	html = re.sub("</?[^bph/].*?/?>", "",html)

	html = re.sub("&.+?;", " ", html)
	html = re.sub("[\t\n \r]{2,}", " ", html)
	html = re.sub("</h> ", "</h>\n<p>", html)

	html_s = html.split("</br>")

	result = ""

	for p in html_s:
		if p != "" and not "|" in p and p != " " and not "ags: " in p:
			result += "<p>" + p + "</p>\n"

	result = re.sub("<.{3,12}>", "", result)

	result = "<html>\n<head><meta http-equiv=\"content-type\" content=\"text/html; charset=UTF-8\" /></head><body>\n<h>" + result + "</body></html>"

	
	if len(sys.argv) > 2 and sys.argv[2] == "true":
		result = re.sub("<.*?>", "", result).strip()

	print result



if __name__ == "__main__":
	main()
