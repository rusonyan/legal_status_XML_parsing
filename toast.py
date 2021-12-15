import json
from logging import log
import smtplib
from email.mime.text import MIMEText
from loguru import logger

import requests

host = 'smtp.email.cn'
user = 'yanruisong@email.cn'
pwd = 'KegAnNBedRWdXtjH'
sender = 'yanruisong@email.cn'
receivers = ['rusonbot@139.com']


def send_mail(title, msg):
    message = MIMEText(msg, 'plain', 'utf-8')
    message['Subject'] = title
    message['From'] = sender
    message['To'] = receivers[0]
    smtpObj = smtplib.SMTP()
    smtpObj.connect(host, 25)
    smtpObj.login(user, pwd)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()


def ding_errow(text):
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=aea29407e29c4cfdbf8023f8fe5daab2ba57b3f88ed229124224e4990dd12937"
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    message = {
        "at": {
            "atMobiles": [
                "15531344258"
            ],
            "isAtAll": False
        },
        "text": {
            "content": text + '--XML解析器'
        },
        "msgtype": "text"
    }
    message_json = json.dumps(message)
    info = requests.post(url=webhook, data=message_json, headers=header)


def ding_send(text):
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=aea29407e29c4cfdbf8023f8fe5daab2ba57b3f88ed229124224e4990dd12937"
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    message = {
        "at": {
            "isAtAll": False
        },
        "text": {
            "content": text + '--XML解析器'
        },
        "msgtype": "text"
    }
    message_json = json.dumps(message)
    info = requests.post(url=webhook, data=message_json, headers=header)


def send(title, msg):
    logger.success(title+msg)
    #ding_send(title+msg)


def send_errow(title, msg):
    #send_mail(title, msg)
    logger.error(msg)
    #ding_errow(title+msg)
