# coding=utf-8
import redis
import datetime
#----------------------------------------------
# 商品收藏数redis查询
#----------------------------------------------
# redis数据库初始化
class Database: 
    def __init__(self): 
        self.host = '192.168.32.30' 
        self.port = 6379 
        self.write_pool = {} 

   
    # 获得每一个key的redis值
    def read(self, key): 
            try: 
                r = redis.StrictRedis(host=self.host, port=self.port) 
                value = r.get(key) 
                # print value 
                return value 
            except Exception, exception: 
                print exception  
    
    # 拿到商品浏览量所有key        
    def getAllKey(self, keysPrefix): 
            try: 
                key = keysPrefix + '_' + '200-*' 
                r = redis.StrictRedis(host=self.host, port=self.port)
                keylist = r.keys(key)
                # print keylist 
                return keylist 
            except Exception, exception: 
                print exception         
    # 拿到指定keys的values        
    def getValuesByKeys(self, keys): 
            try: 
                r = redis.StrictRedis(host=self.host, port=self.port)
                values = r.mget(keys)
                return values 
            except Exception, exception: 
                print exception    

# 读取redis商品浏览量 
def read_data(): 
    """
    startTime = getNow()
    print '开始时间' + str(startTime)
    db = Database() 
    keylist = db.getAllKey('product_id')
    count = 0
    for key in keylist:
        value = db.read(key)
        count = count + 1
        print str(count) + " " + key + '值: ' + value
    endTime = getNow()    
    print '结束时间' + str(endTime)   
    print '耗时：' +str((endTime - startTime).seconds)
    """
    db = Database() 
    keylist = db.getAllKey('product_id')
    values = db.getValuesByKeys(keylist)
    print values
    

    
# 获得当前时间    
def getNow():
    return datetime.datetime.now()

if __name__ == '__main__': 
    read_data()
    
