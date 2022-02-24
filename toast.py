import json
import smtplib
from email.mime.text import MIMEText
import datetime

import requests
from loguru import logger

WEBHOOK = "https://oapi.dingtalk.com/robot/send?access_token=aea29407e29c4cfdbf8023f8fe5daab2ba57b3f88ed229124224e4990dd12937"
ATGROUP = [{"isAtAll": False}, {"atMobiles": ["15531344258"], "isAtAll": False}]


def ding_post(text, isError=0):
    message = {
        "text": {
            "content": text + "\n\nparsing robot   --" + str(datetime.date.today())
        },
        "msgtype": "text",
    }
    message["at"] = ATGROUP[isError]
    info = requests.post(
        url=WEBHOOK,
        data=json.dumps(message),
        headers={"Content-Type": "application/json", "Charset": "UTF-8"},
    )


def send(title, msg=""):
    logger.success(title + msg)
    #ding_post(title + msg)


def send_errow(title, msg=""):
    logger.error(title + msg)
    #ding_post(title + msg, 1)


if __name__ == "__main__":
    send("外观设计事务 (" + "2018-08-02" + ")公报处理完毕!", "共处理" + "12"+ "条数据.")
