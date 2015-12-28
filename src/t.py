import urllib
import urllib2

url = "http://172.16.67.222:8081/c2c/get_myfavorite?user_id=393945&token=a9b61984ba8762eb9e820e54c7a0ebe4"
req = urllib2.Request(url)
print req

res_data = urllib2.urlopen(req)
res = res_data.read()
print res
