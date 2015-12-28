# coding=utf-8
import os, sys, commands
import shutil
dir = "/Users/duwei/百度云同步盘/git"

# 删除指定目录
def removeDir():
    try:
        for root, dirs, files in os.walk(dir, True, None, False):
            if 'target' in root:
                print("The current derectory is:", root)
                files = os.listdir(root)  # 返回目录列表
                for f in files:
                    filepath = os.path.join(root, f)
                    if (os.path.isfile(filepath) == True):  # join 连接目录与文件名
                        print('the file name is: ', os.path.splitext(os.path.join(root, f))[0])
                        os.remove(os.path.join(root, f))  # 删除文件
                    elif os.path.isdir(filepath):
                        shutil.rmtree(filepath, True)
                os.removedirs(root)  # 递归删除空目录 
        # 删除占用空间的目录        
        os.chdir(os.path.join(dir, "workspace"))
        delStr = "rm -rf .metadata"  # 删除字节多的目录
        os.system(delStr)        
    except Exception, e:
        print e
# 调用移除目录方法
removeDir()
