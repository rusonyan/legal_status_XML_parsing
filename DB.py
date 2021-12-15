import cpca
from loguru import logger
import mysql.connector
'''
数据库连接
'''


class DB:
    def __init__(self, publishTime):
        self.cn = mysql.connector.connect(
            host='localhost', port=3306, db='legalState', user='ruson', password='yanruisong',charset='utf8'
        )
        logger.info("此次操作数据库为: legalState")
        self.cursor = self.cn.cursor()
        self.publishTime = publishTime

    def back(self):
        self.cursor.execute('select @@identity')
        return self.cursor.fetchone()


def spilt_address(location, state=True):
    result = cpca.transform([location], pos_sensitive=True).values[0]
    for r in result:
        if r is None:
            state = False
    if state and result[5] != -1:
        return result
    else:
        return list(map(lambda x: None, result))
