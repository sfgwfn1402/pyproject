# coding=utf-8
import os
# file = "/Users/duwei/百度云同步盘/workspace/transaction/cart_api/src/main/resources/conf.properties"
conf_file = "/Users/duwei/Documents/workspace/transaction/cart_api/src/main/resources/conf.properties"
log4j_file = "/Users/duwei/Documents/workspace/transaction/cart_api/src/main/resources/log4j.properties"

#core包属性文件conf.properties日志路径修改
def func_conf():
    input = open(conf_file)
    lines = input.readlines()  # 读取所有内容
    print(lines)
    input.close()
    
    output = open(conf_file, 'w')
    for line in lines:
        if not line:
            break
        if '#log.path' in line:
            temp = line.split("#log.path")
            temp1 = "log.path" + temp[1]
            output.write(temp1)
        elif 'log.path' in line:
            temp = line.split("log.path")
            temp1 = "#log.path" + temp[1]
            output.write(temp1)
        else:    
            output.write(line)
    output.close()
    
#log4j.properties文件日志路径修改    
def func_log4j():
    input = open(log4j_file)
    lines = input.readlines()  # 读取所有内容
    print(lines)
    input.close()
    
    output = open(log4j_file, 'w')
    for line in lines:
        if not line:
            break
        if '#log4j.appender.FILEOUT.File' in line:
            temp = line.split("#log4j.appender.FILEOUT.File")
            temp1 = "log4j.appender.FILEOUT.File" + temp[1]
            output.write(temp1)
        elif 'log4j.appender.FILEOUT.File' in line:
            temp = line.split("log4j.appender.FILEOUT.File")
            temp1 = "#log4j.appender.FILEOUT.File" + temp[1]
            output.write(temp1)
        else:    
            output.write(line)
    output.close()     
    
if __name__ == "__main__":
    func_conf()  # 修改conf.properties
    func_log4j()  # 修改log4j.properties
    
    
    
