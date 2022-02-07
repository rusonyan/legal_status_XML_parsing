import datetime
import ftplib

from loguru import logger

import toast
from config import MAX_RETRY
from request_control import request_controller, delay_time

"""
主程序
"""

logger.add("log/运行日志.log", encoding="utf-8", rotation="00:00")

if __name__ == "__main__":
    state = 0
    try:
        while state < MAX_RETRY:
            try:
                request_controller(state)
                break
            except ftplib.error_temp as e:
                logger.error(str(state) + "次登录失败  " + str(e))
                delay_time()
                state += 1
        toast.send(
            "😿😿  多次尝试登录但是始终无法登录  --", str(datetime.date.today())
        ) if state == MAX_RETRY else logger.success("--------END--------")
    except OSError as e:
        toast.send_errow("socket超时", str(e))
    except Exception as e:
        toast.send_errow("XML解析发生未知错误!", str(e))
