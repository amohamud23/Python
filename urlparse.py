from urllib.parse import urlparse
url = "http://www.mail.inbox.yahoo.com.us"

r1 = urlparse(url).hostname.split('.')[3]
print (r1)
