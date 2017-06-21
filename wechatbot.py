# -*- coding: utf-8 -*-
import werobot
from werobot.replies import ImageReply

robot = werobot.WeRoBot(token='yoyo')


# @robot.text 修饰的 Handler 只处理文本消息
@robot.text
def turing(message):
    url="http://www.tuling123.com/openapi/api"
    data={
        'key':'78b9fc3edc4f4ba782bfbeb32497b952',
        'info':message.content,
        'userid': '12345678',
    }
    return requests.post(url,data=data).json()['text']

# @robot.image 修饰的 Handler 只处理图片消息
@robot.image
def img(message):
    return ImageReply(message=message, media_id=message.MediaId)


# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()