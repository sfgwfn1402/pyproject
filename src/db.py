# coding=utf-8
import threading
'''
数据库引擎对象：
'''
class _Engine(object):  # 继承object类
    
    # 初始化方法(相当于构造方法)，绑定类成员connect
    # self创建实例本身
    def __init__(self, connect):
        self._connect = connect
    
    # 返回数据库连接
    def connect(self):
        return self._connect()
    
engine = None

'''
持有数据库连接的上下文对象
'''
class _DbCtx(threading.local):
    # 初始化方法
    def __init__(self):
        self.connection = None
        self.transactions = 0
    
    # 判断数据库连接为空时，返回true
    def is_init(self):
        return not self.connection is None
    
    # 获得数据库连接
    def init(self):
        self.connection = 0 #_LasyConnection()
        self.transactions = 0
        
    # 释放数据库连接
    def cleanup(self):
        self.connection.cleanup()    
        self.connection = None
    
    # 数据库连接游标
    def cursor(self):
        return self.connection.cursor()
    
# 创建对象(threadlocal对象)
_db_ctx = _DbCtx()    

'''
数据库连接类
'''
class _ConnectionCtx(object):
    
    # 1.创建数据库连接
    def __enter__(self):
        global _db_ctx  # 全局变量，在方法内部可以改变变量值
        self.should_cleanup = False
        
        if not _db_ctx.is_init():  # 判断数据库连接为空时执行
            _db_ctx.init()
            self.should_cleanup = True
        return self
    
    # 2.释放数据库连接
    def __exit__(self, exctype, excvalue, traceback):
        global _db_ctx
        if self.should_cleanup:
            _db_ctx.cleanup()
'''
返回创建的数据库连接对象
'''
def connection():
    return _ConnectionCtx()


'''
事务类
'''
class _TransactionCtx(object):
    
    # 获得连接并开启新事务
    def __enter__(self):
        global _db_ctx
        self.should_close_conn = False
        if not _db_ctx.is_init():  # 数据库连接为空则执行
            _db_ctx.init()  # 获得数据库连接
            self.should_close_conn = True
        _db_ctx.transactions = _db_ctx.transactions + 1    
        return self    

    # 退出当前事务
    def __exit__(self, exctype, excvalue, traceback):
        global _db_ctx
        _db_ctx.transactions = _db_ctx.transactions - 1
        try:
            if _db_ctx.transactions == 0:
                if exctype is None:
                    self.commit()
                else:
                    self.rollback()    
        finally:
            if self.should_close_conn:
                _db_ctx.cleanup()
    
    # 提交数据库
    def commit(self):
        global _db_ctx
        try:
            _db_ctx.connection.commit()
        except:
            _db_ctx.connection.rollback()
            raise  # 当程序出现错误，python会自动引发异常，也可以通过raise显示地引发异常。一旦执行了raise语句，raise后面的语句将不能执行

    def rollback(self):
        global _db_ctx
        _db_ctx.connection.rollback()




















