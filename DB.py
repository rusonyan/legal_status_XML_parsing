import re
from datetime import datetime

import cpca
import mysql.connector
from loguru import logger

"""
数据库连接
"""


def split_patent(str):
    result = re.findall(r"ZL ([0-9a-zA-Z.\d]{10,14})", str)[0]
    if result is None:
        raise Exception("专利号错误")
    else:
        return result


class DB:
    def __init__(self, publishTime):
        self.cn = mysql.connector.connect(
            host="localhost",
            port=3306,
            db="legalState",
            user="ruson",
            password="yanruisong",
            charset="utf8",
        )
        logger.debug("此次操作数据库为：测试库")
        self.cursor = self.cn.cursor()
        self.publishTime = publishTime

    def back(self):
        self.cursor.execute("select @@identity")
        return self.cursor.fetchone()

    def end(self):
        self.cursor.execute(
            "INSERT INTO  change_db_log VALUES (%s,%s,%s,%s)",
            (0, datetime.now(), self.publishTime, None),
        )


def spilt_address(location):
    return cpca.transform(
        [location],
    ).values[0]
