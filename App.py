import ftplib
import sys
from loguru import logger
import toast
from FTP import Ftp
from Unzip import unzip_file
from xml_to_node import locate_XML_file
'''
主程序
'''

Local = r'/home/yrs/history/'
logger.add("running.log")

@logger.catch
def main():
    RemoteNames = find_new_file()
    if RemoteNames is None:
        toast.send('今天无XML更新鸭！', '今天无XML更新鸭！')
    else:
        paths = list(map(lambda x: Local + x, RemoteNames))
        for path in paths:
            unzip_file(path)
            locate_XML_file(path)
        toast.send('此次解析数据公开日为'+str(RemoteNames), '解析成功')

def find_new_file():
    ftp = Ftp()
    RemoteNames = ftp.DownLoadFileTree(
        Local, 'SIPO/CN-PA-PRSS-30 中国外观设计专利法律状态标准化数据/'.encode("utf-8").decode(
            "latin1"))
    ftp.close()
    return RemoteNames


try:
    main()
except ftplib.error_temp as e:
    toast.send('FTP服务器人数过多！', str(e))
except Exception as e:
    toast.send_errow('XML解析出错啦！！', str(e))
logger.success('-------------------------------')