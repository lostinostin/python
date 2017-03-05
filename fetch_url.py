# Builds the UA array
ualist = []
def genUaList():
	import requests,urllib2
	r = requests.get('http://www.useragentstring.com/pages/useragentstring.php')
	content = r.content

	from bs4 import BeautifulSoup
	from pprint import pprint
	ua_main_page_list = []
	soup	= BeautifulSoup( content , "html.parser")
	for link in soup.find_all('a'):
		ua_main_page_list.append("http://www.useragentstring.com"+link.get('href'))

	#del	uapagelist[0:6]
	ua_main_page_list = [x for x in ua_main_page_list if "useragentstring.php?name" in x]
#	pprint(uapagelist)
	
	for uaMainPageUrl in ua_main_page_list:
		uareq = requests.get(uaMainPageUrl)
		ua_main_page_content = uareq.content
		
		
		soupDos = BeautifulSoup( ua_main_page_content , "html.parser" )
		
		rel_a_tag_urls = []
		for a in soupDos.find_all('a'):
			rel_a_tag_urls.append("http://www.useragentstring.com"+a.get('href'))
			rel_a_tag_urls = [x for x in rel_a_tag_urls if "index.php?id" in x]
			
#		print rel_a_tag_urls
		for uaPageUrl in rel_a_tag_urls:
			ua_page_req = requests.get(uaPageUrl)
			ua_page_content = ua_page_req.content

			soupTres = BeautifulSoup( ua_page_content , "html.parser")

			for b in soupTres.find(id="uas_textfeld"):
				ualist.append(b)
				print b
	uafile = open('/Users/chris.crawford/pythonProjects/uaList.txt', 'w')
	for ua in ualist:
		  uafile.write("%s\n" % ua)
		#pprint(a_tags)
#		ua_string.find_parents("a")

			#uaStringUrlList.append(
#			try:
#				print(href.get_text())
#			except requests.exceptions.ConnectionError:
#				uareq.status_code = "Connection refused"
#	pprint(uaStringUrlList)
	#a_tags = soup.find_all('a')
	#for text in a_tags:
	#	print(text.get(soup.get_text())
	
genUaList()

# print ualist

# Scrambles the UA string that's sent in a request header
def scrambleUaList():

	import urllib2,cookielib,json

	#userin 	= raw_input('url: ')
	ua		= 'http://www.useragentstring.com/pages/useragentstring.php'
	# site	= userin
	hdr		= {
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
			'Accept-Encoding': 'none',
			'Accept-Language': 'en-US,en;q=0.8',
			'Connection': 'keep-alive'
			}
	req 	= urllib2.Request(site, headers=hdr)

	try:
		page = urllib2.urlopen(req)
	except urllib2.HTTPError, e:
		print e.fp.read()

	content	= page.read()

	from bs4 import BeautifulSoup
	from pprint import pprint

	soup	= BeautifulSoup( content , "html.parser")
	ualist = []
	for link in soup.find_all('a'):
		ualist.append("http://www.useragentstring.com"+link.get('href'))

	pprint(ualist)
