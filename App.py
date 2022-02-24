import datetime
import ftplib
import sys
import traceback

from loguru import logger

import toast
from config import MAX_RETRY
from request_control import request_controller, delay_time

"""
主程序
"""

logger.add("log/运行日志.log", encoding="utf-8", rotation="00:00", retention="5 days")

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
            except OSError as e:
                logger.error(
                    str(state)
                    + "次socket超时  "
                    + str(traceback.extract_tb(sys.exc_info()[2]))
                )
                delay_time()
                state += 1
        toast.send("CNIPA服务已达最大登录限制") if state == MAX_RETRY else logger.success(
            "--------END--------"
        )
    except Exception as e:
        toast.send_errow("ERROR!", str(e))
