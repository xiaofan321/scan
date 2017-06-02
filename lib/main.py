# coding=utf-8
from Queue import Queue
import sys
import options
import getTask
import scan
import tools


def scanpoc():

    try:
        # 获取参数
        args = options.oparser()

        # 获取任务
        qtask = getTask.getTask(args.urls,args.pocfile)

        # 启动扫描
        qresults = Queue()
        scan.main(qtask,qresults,args.thread)

        # 保存结果
        if args.out:
            tools.set2txt(args.out,qresults)

    except TypeError as e:
        print e
        sys.exit(0)
    except Exception as e:
        print e
        sys.exit(0)

    
    
scanpoc()


