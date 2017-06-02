# coding=utf-8
from threading import Thread
from Queue import Queue
import imp
import getTask

class Pocscan(Thread):
    def __init__(self,qtasks,qresults):
        Thread.__init__(self)
        self.qtasks = qtasks
        self.qresults = qresults

    def run(self):
        while True:
            try:
                url,poc = self.qtasks.get(True,0.01)
                self.scan(url,poc)
            except Exception,e:
                self.qtasks.task_done()
                print 'Exception==>',e
                break


    def scan(self,url,poc):
        # print url,poc
        pocscan = imp.load_source('util', poc)
        result = pocscan.Pocscan(url).verify()
        if result['status'] :
            self.qresults.put(result)
            print result['info']
        else:
            print 'fail'


def main(qtask,qresults,ath):
    qsize = qtask.qsize()
    thnum = ath if ath else 30
    thnums = thnum if thnum < qsize else qsize

    threads = [Pocscan(qtask,qresults) for _ in range(thnums)]

    #启动线程
    for t in threads:
        t.start()

    #线程阻塞（全部线程执行完后再往下运行。）
    for t in threads:
        t.join()



if __name__ == '__main__':

    # qtask = getTask.getTask('http://www.baidu.com','../payload/phpcms')
    qtask = getTask.getTask(r'C:\Users\Administrator\Desktop\urls.txt','../payload/common')
    qresults = Queue()
    main(qtask,qresults,10)

    # while not qresults.empty():
    #     print qresults.get()['info']