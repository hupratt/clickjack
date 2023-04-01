import os
import sys
import webbrowser

if len(sys.argv) != 2:
	print('\n[+] Description: %s can quickly verify if a web page is vulnerable to clickjacking' % __file__)
	print('[+] Usage: python %s <url>\n' % __file__)
	exit(0)

url = sys.argv[1]

html = '''
<html>
	<head>
		<title>Clickjacking Test Page</title>
	</head>

	<body>
		<h1>Clickjacking Test Results</h1>
		<h2>Target: <a href="%s">%s</a></h2>
		<iframe width="900" height="600" src="%s"></iframe>
	</body>
</html>
''' % (url, url, url)


cjt = os.path.abspath('cj-target.html')
localurl = 'file://' + cjt

with open(cjt, 'w') as t:
	t.write(html)

webbrowser.open(localurl)

print('\n[+] Test Complete!')
