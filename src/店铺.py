import urllib,json,urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf8')
url="https://115.182.236.5/api/shop/shop_detail.json?userId=661&clientOs=1&clientOsVersion=4.3&appType=1&appVersion=1.0&phoneType=%E4%B8%89%E6%98%9FGALAXY+Note4&ip=192.12.33.22&mac=ac+as+23+3d&netType=4G&devId=IPhone123456789&otherDevInfo=someInfo&loginToken=W29GFvjsC6120Cp9u76Y31F6&pageNum=1&numPerPage=10&lastRecordId=1000001"
params={"shopId":146}
par=urllib.urlencode(params)
request=urllib2.Request(url,par)
request=urllib2.urlopen(request).read()
result=json.loads(request)
res=result.get("data")
for m,n in result.items():
    print m,n
for i,j in res.items():
    print ("%s:%s")%(i,j)