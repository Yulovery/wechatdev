# -*- coding: utf-8 -*-
import werobot
from werobot.replies import ImageReply
import requests
import urllib, cStringIO
from PIL import Image

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
    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    # 将256灰度映射到70个字符上
    def get_char(r,g,b,alpha = 256):
        if alpha == 0:
            return ' '
        length = len(ascii_char)
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
        unit = (256.0 + 1)/length
        return ascii_char[int(gray/unit)]
    file = cStringIO.StringIO(urllib.urlopen(message.img).read())
    im = Image.open(file)
    print (type (message.img))
    im = im.resize((24,24), Image.NEAREST)
    txt = ""
    for i in range(24):
        for j in range(24):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    #return ImageReply(message=message, media_id=message.MediaId)
    print txt
    return txt


# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()