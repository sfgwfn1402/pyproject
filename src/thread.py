# coding=utf-8
import time, threading
# 启动一个线程就是把函数传入并创建Thread实例，然后调用start()开始执行
# 新线程执行的代码：
def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name     




print 'thread %s is running...' % threading.current_thread().name

# 线程参数：传入函数，线程名字
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name


