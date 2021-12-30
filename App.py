import ftplib
import os
import sys
import time
from loguru import logger
import random
import toast
from FTP import Ftp
from Unzip import unzip_file
"""
主程序
"""

MAX_RETRY = 4
MINI_CONNECT_TIME = 1000
MAX_CONNECT_TIME = 3000
LOCAL_FOLDER = r'/home/yrs/history/'
REMOTE_FOLDER = r"SIPO/CN-PA-PRSS-30 中国外观设计专利法律状态标准化数据/".encode("utf-8").decode(
    "latin1"
)
logger.add("running.log", encoding="utf-8")


def main(state):
    ftp = Ftp(LOCAL_FOLDER, REMOTE_FOLDER)
    RemoteNames = ftp.find_raw_data()
    if RemoteNames is None:
        toast.send("今天无XML更新鸭!🙌", "今天无XML更新鸭!🙌")
    else:
        for folder in RemoteNames:
            while state < MAX_RETRY:
                try:
                    single_floder(ftp, folder)
                    toast.send("😽😽 数据公开日" + str(folder), "解析成功")
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


def single_floder(ftp, folder):
    LocalDir = os.path.join(LOCAL_FOLDER, folder)
    ftp.login()
    ftp.download_folder(LocalDir, folder)
    ftp.close()
    unzip_file(LocalDir)

def delay_time():
    delay_time=random.randint(MINI_CONNECT_TIME, MAX_CONNECT_TIME)
    logger.debug("等待" + str(delay_time) + "秒")
    time.sleep(delay_time)

state = 0
try:
    while state < MAX_RETRY:
        try:
            main(state)
            break
        except ftplib.error_temp as e:
            logger.error(str(state) + "次登录失败  " + str(e))
            delay_time()
            state += 1
    toast.send("😿😿  多次尝试登录但是始终", "登录失败") if state == MAX_RETRY else logger.success(
        "--------END--------"
    )
except Exception as e:
    toast.send_errow("XML解析发生未知错误!", str(e))
