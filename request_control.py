import datetime
import ftplib
import os
import random
import sys
import time

from loguru import logger

import toast
from FTP import Ftp
from Unzip import unzip_file
from config import (
    LOCAL_FOLDER,
    REMOTE_FOLDER,
    MAX_RETRY,
    MINI_CONNECT_TIME,
    MAX_CONNECT_TIME,
)
from xml_to_node import locate_XML_file

"""
FTP请求控制
"""


def request_controller(state):
    ftp = Ftp(LOCAL_FOLDER, REMOTE_FOLDER)
    RemoteNames = ftp.find_raw_data()
    if RemoteNames is None:
        toast.send("无更新 --", str(datetime.date.today()))
    else:
        polling_control(RemoteNames, ftp, state)


def polling_control(RemoteNames, ftp, state):
    for folder in RemoteNames:
        while state < MAX_RETRY:
            try:
                single_flooder_handle(ftp, folder)
                break
            except ftplib.all_errors as e:
                logger.error("下载" + folder + "失败  " + str(e))
                delay_time()
                state += 1
        if state < MAX_RETRY:
            delay_time()
        else:
            toast.send("部分数据", "请求失败")
            sys.exit(0)


def single_flooder_handle(ftp, folder):
    LocalDir = os.path.join(LOCAL_FOLDER, folder)
    ftp.login()
    ftp.download_folder(LocalDir, folder)
    ftp.close()
    unzip_file(LocalDir)
    count = locate_XML_file(LocalDir)
    toast.send("外观设计事务(" + str(datetime.datetime.strptime(str(folder), '%Y%m%d').date()) + ")公报处理完毕,", "共处理" + str(count) + "条数据.")


def delay_time():
    delaying = random.randint(MINI_CONNECT_TIME, MAX_CONNECT_TIME)
    logger.debug("等待" + str(delaying) + "秒")
    time.sleep(delaying)
