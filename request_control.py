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
from config import LOCAL_FOLDER, REMOTE_FOLDER, MAX_RETRY, MINI_CONNECT_TIME, MAX_CONNECT_TIME
from xml_to_node import locate_XML_file

"""
FTP请求控制
"""


def request_controller(state):
    ftp = Ftp(LOCAL_FOLDER, REMOTE_FOLDER)
    RemoteNames = ftp.find_raw_data()
    if RemoteNames is None:
        toast.send("未发现XML更新!🙌 --", str(datetime.date.today()))
    else:
        polling_control(RemoteNames, ftp, state)


def polling_control(RemoteNames, ftp, state):
    for folder in RemoteNames:
        while state < MAX_RETRY:
            try:
                single_flooder_handle(ftp, folder)
                toast.send("😽😽 数据公开日" + str(folder), "解析成功!")
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
    locate_XML_file(LocalDir)


def delay_time():
    delaying = random.randint(MINI_CONNECT_TIME, MAX_CONNECT_TIME)
    logger.debug("等待" + str(delaying) + "秒")
    time.sleep(delaying)
