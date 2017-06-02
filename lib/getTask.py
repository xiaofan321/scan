# coding=utf-8
from Queue import Queue
import os

def getTask(urls,pocpath):

    # 获取url列表
    lurl = []
    if os.path.isfile(urls):
        with open(urls) as f:
            for line in f:
                lurl.append(line.strip())
    elif 'http' in urls or 'www' in urls :
        lurl.append(urls.strip())
    else:
        raise TypeError('-u content is invalid !')


    # 获取poc 列表
    lpoc = []
    if os.path.isdir(pocpath):
        for root, dirs, files in os.walk(pocpath):
            for name in files:
                if name.endswith('.py') and not name.startswith('__'):
                    lpoc.append(os.path.join(root, name))
    elif os.path.isfile(pocpath):
        lpoc.append(pocpath)
    else:
        raise TypeError('-r content is invalid !')

    # 生成数据
    qtask = Queue()
    for url in lurl:
        for poc in lpoc:
            qtask.put((url,poc))

    return qtask


if __name__ == '__main__':
    task = getTask('http://www.baidu.com','.')
    while not task.empty():
        print task.get() 