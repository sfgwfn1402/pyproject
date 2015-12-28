# coding=utf-8
import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='orcl', db='mysql', port=3306)
    cur = conn.cursor()
    count = cur.execute('select * from user')
    print "there has %s rows record" %count
    cur.close()
    conn.close()
except Exception, e:
    print "Mysql Error %d: %s" %(e.args[0], e.args[1])
