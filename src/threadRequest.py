# coding=utf-8
import time, threading
import urllib
import urllib2

url = "http://172.16.67.222:8081/c2c/get_myfavorite?user_id=393945&token=a9b61984ba8762eb9e820e54c7a0ebe4"
req = urllib2.Request(url)

def request():
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res
    
def run_thread(n):
    for i in range(1000):
        request()    

for j in range(1):
    t1 = threading.Thread(target=run_thread, args=(5,))
    t1.start()
