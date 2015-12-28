# coding=utf-8
import os, sys, commands
#购物车Tomcat路径
tomcat_path = "/Users/duwei/Documents/data/webserver/tomcat-cart-8083/"
#购物车打包生成war路径
cartSourcePath = "/Users/duwei/Documents/data/source/transaction/cart_api/target/*.war"
#购物车部署路径
cartDeploymentPath = "/Users/duwei/Documents/data/web/java/cartapi/"


# 1.从svn更新项目代码【--no-auth-cache：防止缓存的认证信息（如用户名和密码在Subversion运行时配置目录）。 】
def updateSvn(strUser, strPwd):
    strExec = "svn up --username %s --password %s --no-auth-cache" % (strUser, strPwd)
    print("Perform the update command line: %s" % strExec)
    # 执行命令
    nResult = os.system(strExec)
    print("nRet = %d" % nResult)
    return (0 == nResult)

# 2.从svn检出项目代码
def packageSvn(strUser, strPwd, strUpPath):
    strExec = "svn co %s --username %s --password %s" % (strUpPath, strUser, strPwd)
    print("Perform the checkout command line: %s" % strExec)
    # 执行命令
    nResult = os.system(strExec)
    print("nRet = %d" % nResult)
    return (0 == nResult)

# 3.打包项目
def package():
    strExec = "source ~/.bash_profile; mvn clean; mvn package -Dmaven.test.skip=true"
    nResult = os.system(strExec)
    return (0 == nResult)

# 4.购物车Tomcat启动
def rebootCartTomcat():
    pid = "ps aux | grep 'tomcat-cart-8083/conf' | grep -v grep | awk '{print $2}'"
    (status, output) = commands.getstatusoutput(pid)  # 返回对值（状态值，输出值）
    print status, output
    print("tomcat-cart-8083 PID is %s" % status)
    if not output:
        print "购物车Tomcat没有启动，无需停止操作."
    else:
        killPID(output)  # 停止购物车Tomcat服务
    strExec = "sh %s/bin/startup.sh" % tomcat_path
    nResult = systemExe(strExec)
    if nResult == 0:
        loginfo = "tail -f %s/logs/catalina.out" % tomcat_path
        systemExe(loginfo)        
# 5.将购物车war拷贝到指定目录，并解压war包
def copyCartWar():
    
    strExec = "cp %s %s/cart.war" % (cartSourcePath, cartDeploymentPath)
    nResult = os.system(strExec)
    if nResult == 0:
        currentDerectory = os.getcwd()
        print "The current derectory is %s" % currentDerectory 
        os.chdir(cartDeploymentPath)
        delStr = "ls | grep -v cart.war | xargs rm -rf"  # 删除购物车信息
        os.system(delStr)
        unzipStr = "unzip %s/cart.war -d %s" % (cartDeploymentPath, cartDeploymentPath) 
        os.system(unzipStr)
    return (0 == nResult)

def killPID(PID):
    strExec = "kill -9 %s" % PID
    nResult = os.system(strExec)
    return (0 == nResult)

# 执行命令操作
def systemExe(strExec):
    nResult = os.system(strExec)
    return nResult

# 请输入数字
def numberInput():
    v = raw_input("Please input: ")
    while True:
        if v in '\r\n':
            print "不能回车，请输入数字！"
        elif v == '\b':    
            print "不能退格，请输入数字！"
        elif v.isdigit() == False:
            print "请输入数字！"
        else:
            break
        v = raw_input("Please input: ")
    return int(v)

# svn检出状态
def checkoutStatus(bUp):
    if bUp:
        print("svn checkout/update success.")
    else:
        print("svn checkout/update failed!")

# 全局变量
source_path = "/Users/duwei/Documents"

# 本文件执行时生效，在别的文件引用该文件，下面条件不会生效；因为__name__变成了引用该文件的文件自己的名称
if "__main__" == __name__:
    
    print("Please select db sequence number")
    print("--------------------------------")
    print("1. 自动部署并启动Tomcat")
    print("2. 手动部署并启动Tomcat")
    print("--------------------------------")
    try:
        v = numberInput()
        if v == 1:
            print "开始自动部署..."
            bUp = False
            detectionDirectory = "transaction"
            command = '/Users/duwei/Documents/data/source/'
            os.chdir(command)  # 跳转目录
            project_path = os.path.join(command, detectionDirectory)  # 连接目录
            # 第一步：svn检出项目代码
            if os.path.isdir(project_path) == True:
                print "1. The trade project begin update."
                os.chdir(detectionDirectory)
                bUp = updateSvn("duwei", "duwei0910")  # 更新
            else:
                print "1. The trade project begin checkout."
                bUp = packageSvn("duwei", "duwei0910", "http://svn.yunmall.com/svn/dev/transaction_liequ/transaction_lq_spring/ transaction")
                os.chdir(detectionDirectory)
            checkoutStatus(bUp)
            # 第二步：打包交易项目
            pf = package()
            if pf:
                copyCartWar()
            
            # 第三步：启动cartTomcat服务
            rebootCartTomcat()
            
        elif v == 2:
            print "开始手动部署..."    
        else:
            print "输入错误，退出."    
            sys.exit(1) 
    except Exception, e:
        print e
    finally:
        print 'The program running finish.'
