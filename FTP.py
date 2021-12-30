import ftplib
from logging import log
from re import S
import time
import pickle
from loguru import logger
import os
'''
FTP更新
'''
def history_add(str):
    history=get()
    history.add(str)
    with open('.history', 'wb') as f:
        pickle.dump(history, f)


def put(tuple):
    with open('.history', 'wb') as f:
        pickle.dump(tuple, f)


def get():
    with open('.history', 'rb') as f:
        return pickle.load(f)


class Ftp:
    ftp = ftplib.FTP()

    def __init__(self,Local,Remote):
        self.ftp.set_debuglevel(2)
        self.Local=Local
        self.Remote=Remote   
        self.ftp.connect(host='patdata2.cnipa.gov.cn', port=21,timeout=1200)
        self.ftp.login('xxzx_yingmaiqi', 'yingmaiqi1.')
    
    def login(self):
        self.ftp.connect('patdata2.cnipa.gov.cn', 21)
        self.ftp.login('xxzx_yingmaiqi', 'yingmaiqi1.')
 
    def close(self):
        self.ftp.quit()
        logger.info("ftp退出")

    def find_raw_data(self):
        self.ftp.cwd(self.Remote)
        RemoteNames = self.ftp.nlst()
        newSet = set(RemoteNames) - get()
        logger.debug("远程服务器的所有文件列表:"+str(RemoteNames))
        logger.debug("本次要下载的文件列表:"+str(newSet))
        # put(set(RemoteNames))
        # newSet=set(RemoteNames)-set(RemoteNames)
        new_list=list(newSet)
        new_list.sort()
        if len(new_list) is 0:
            return None       
        else:
            return new_list
    

    def download_file(self, LocalFile, RemoteFile):
        file_handler = open(LocalFile, 'wb')
        logger.info(file_handler)
        self.ftp.retrbinary('RETR ' + RemoteFile, file_handler.write)
        file_handler.close()
        logger.info("下载完成")
        return True
    

    def download_folder(self, LocalDir, folder):
        RemoteDir=os.path.join(self.Remote, folder)
        if not os.path.exists(LocalDir):
            os.makedirs(LocalDir)
        self.ftp.cwd(RemoteDir)
        RemoteNames = self.ftp.nlst()
        logger.info(folder+"的文件夹文件列表:"+str(RemoteNames))
        for file in RemoteNames:
            Local = os.path.join(LocalDir, file)
            if file.find(".") == -1:
                logger.error(RemoteDir)
            elif file.endswith('.ZIP'):
                logger.info("正在下载:"+file)
                if self.download_file(Local, file):
                    history_add(folder)
            else:
                pass

