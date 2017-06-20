# -*- coding: utf-8 -*-
# filename: handle.py
import hashlib
import reply
import receive
import web
import requests

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "yoyo" #请按照公众平台官网\基本配置中信息填写

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument

    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData   #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    content = recMsg.Content
                    #print content, type(content)
                    if content[0:7] == 'weather':
                        cityname=content[0:-2]
                        params ={'cityname': cityname, 'key': '59c4d4057feed1a7ac32e7055ae7d849'}
                        url = 'http://v.juhe.cn/weather/index'
                        resp = requests.get(url, params=params)
                        weather = resp.json()['result']['today']['weather']
                        info = resp.json()
                        print info
                        content = weather.encode('utf-8')
                        #content[0;2] == "天气" or 
                    else:
                        pass
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                elif recMsg.MsgType == 'image':
                    Images = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, Images)
                return replyMsg.send()
            else:
                print "暂且不处理"
                return "success"
        except Exception, Argment:
            return Argment
