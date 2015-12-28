# coding=utf-8
'''
读取文件内容，取得字符串出现的次数
'''

# f = open("/Users/duwei/Documents/log/trade_api/trade.2015-03-26-11.log")  # 返回一个文件对象
# 数据字典
strs = {"dependent":0, "bean":0}

# 处理一般文件
'''
line = f.readline()  # 调用文件的 readline()方法
while line:
    # 将每行内容按空格分隔成texts数组
    texts = line.split(" ")
    for i in range(len(texts)):  # 循环要查询的内容数组
        for sum in strs:  # 循环要统计的数据字典 
            if texts[i] == sum:
                strs[sum] = strs[sum] + 1
                print line
    # print line,  # 后面跟 ',' 将忽略换行符
    # print(line, end = '')　　　# 在 Python 3中使用
    line = f.readline()
'''    
    
# 可处理大文件
with open('/Users/duwei/Documents/log/trade_api/trade.2015-03-26-11.log', 'r') as f:
    for line in f:
        # line.process
         # 将每行内容按空格分隔成texts数组
        texts = line.split(" ")
        for i in range(len(texts)):  # 循环要查询的内容数组
            for sum in strs:  # 循环要统计的数据字典
                if texts[i] == sum:
                    strs[sum] = strs[sum] + 1
                    print line
        # print line,  # 后面跟 ',' 将忽略换行符
        # print(line, end = '')　　　# 在 Python 3中使用
        # line = f.readline()
    
print(strs)
f.close()
