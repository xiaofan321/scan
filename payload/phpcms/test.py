#coding=utf-8
import requests

class Pocscan(object):
    def __init__(self,target):
        self.target = target
        self.result = {
            "name": "phpcms sqli",
            "version": "9.6.0",
            "status":False,
            "info":"",
        }

    def verify(self):
        req = requests.get(self.target,timeout=5)
        if 'a' in req.text:
            self.result['status'] = True
            self.result['info'] = "target: | %s | have %s" %(self.target,self.result['name']) 
        return self.result
       
