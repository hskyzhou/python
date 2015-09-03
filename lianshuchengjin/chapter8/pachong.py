#encoding = utf-8
import urllib2
import re
import threading
import time

proxyLists = []    # 代理ip列表(未验证)
proxyCheckedLists = []  #验证的代理ip列表
proxyLock = threading.RLock() # 获取一个锁

class HskyProxy:
    '''
    http://www.itmop.com/proxy/post/1890.html
    '''
    def __init__(self):
        self.proxyUrl = "http://www.itmop.com/proxy/post/1890.html"
        self.preg = re.compile(r'''<p>代理IP地址 端口 代理位置 是否匿名 类型 验证时间 <br />(.+?)</p>''')
        self.proxyLists = []
        
    
    def getProxy(self):
        result = urllib2.urlopen(url=self.proxyUrl)
        res = result.read()
        matchs = self.preg.findall(res)
        match_lists = matchs[0].split('<br />')
        for ml in match_lists:
            proxyRow = ml.replace("&nbsp;", "").split(" ")            
            ip = proxyRow[0] #ip
            port = proxyRow[1] #port 端口
            address = proxyRow[2] #服务器地址
            securty = proxyRow[3] #安全性
            agent = proxyRow[4] # 代理
            l = [ip, port, address, securty, agent]
            self.proxyLists.append(l)

'''
写一个类  继承  线程类
处理 验证  代理是否可用
公用对象
'''

class HskyProxyCheck(threading.Thread):
    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.test_url = "http://www.baidu.com"
        self.test_str = "030173"
        self.timeout = 5
    def run(self):
        global proxyLists
        global proxyCheckedLists
        while proxyLists:
            proxyLock.acquire()  #获取锁
            proxyList = proxyLists.pop() #推出一个代理ip信息
            proxyLock.release()
            
            cookie = urllib2.HTTPCookieProcessor()  #使用cookie
            proxyHandle = urllib2.ProxyHandler({"http" : r"http://%s:%s" % (proxyList[0], proxyList[1])})
            opener = urllib2.build_opener(cookie, proxyHandle)
            opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.102 Safari/537.36")]
            urllib2.install_opener(opener)
            t1 = time.time()
            try:
                req = urllib2.urlopen(self.test_url, timeout=self.timeout)
                result = req.read()
                pos = result.find(self.test_str)
                timeused = time.time() - t1
                proxyList.append(timeused)
                if pos > 1:
                    proxyLock.acquire()
                    proxyCheckedLists.append(proxyList)
                    proxyLock.release() 
            except Exception,e:
                continue
            

if __name__ == '__main__':
    pro_start = time.time()
    hskyProxy = HskyProxy()
    hskyProxy.getProxy()
    proxyLists = hskyProxy.proxyLists  # 代理ip
    #定义2个线程
    proxyCheckThread1 = HskyProxyCheck("1")
    proxyCheckThread2 = HskyProxyCheck("2")
    proxyCheckThread3 = HskyProxyCheck("3")
    proxyCheckThread4 = HskyProxyCheck("4")
    proxyCheckThread5 = HskyProxyCheck("5")
    proxyCheckThread6 = HskyProxyCheck("6")
    
    proxyCheckThread1.start()
    proxyCheckThread2.start()
    proxyCheckThread3.start()
    proxyCheckThread4.start()
    proxyCheckThread5.start()
    proxyCheckThread6.start()
    
    proxyCheckThread1.join()
    proxyCheckThread2.join()
    proxyCheckThread3.join()
    proxyCheckThread4.join()
    proxyCheckThread5.join()
    proxyCheckThread6.join()
    
    fp = open("proxy.txt", "w+")
    for proxy in proxyCheckedLists:
        fp.write("%s:%s\t%s\t%s\t%s\n" % (proxy[0], proxy[1], proxy[2], proxy[3], proxy[4]))
    
    pro_end = time.time()
    print pro_end - pro_start
    