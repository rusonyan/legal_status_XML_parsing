import ftplib
import time
import pickle
from loguru import logger
import os
'''
FTP更新
'''


def put(tuple):
    with open('.history', 'wb') as f:
        pickle.dump(tuple, f)


def get():
    with open('.history', 'rb') as f:
        return pickle.load(f)


class Ftp:
    ftp = ftplib.FTP()

    def __init__(self):
        self.ftp.connect('patdata2.cnipa.gov.cn', 21)
        self.ftp.login('xxzx_yingmaiqi', 'yingmaiqi1.')


    def DownLoadFile(self, LocalFile, RemoteFile):
        time.sleep(10)
        file_handler = open(LocalFile, 'wb')
        logger.info(file_handler)
        self.ftp.retrbinary('RETR ' + RemoteFile, file_handler.write)
        file_handler.close()
        return True

    def DownLoadFileTrees(self, LocalDir, RemoteDir):
        if not os.path.exists(LocalDir):
            os.makedirs(LocalDir)
        self.ftp.cwd(RemoteDir)
        RemoteNames = self.ftp.nlst()
        for file in RemoteNames:
            Local = os.path.join(LocalDir, file)
            if file.find(".") == -1:
                if not os.path.exists(Local):
                    os.makedirs(Local)
                self.DownLoadFileTrees(Local, file)
            else:
                self.DownLoadFile(Local, file)
        self.ftp.cwd("..")
        return RemoteNames

    def DownLoadFileTree(self, LocalDir, RemoteDir):
        if not os.path.exists(LocalDir):
            os.makedirs(LocalDir)
        self.ftp.cwd(RemoteDir)
        RemoteNames = self.ftp.nlst()
        newSet = set(RemoteNames) - get()
        logger.debug("远程服务器的所有文件列表:"+str(RemoteNames))
        
        # put(set(RemoteNames))
        # newSet=set(RemoteNames)-set(RemoteNames)
        if len(newSet) is 0:
            return None
        else:
            for file in newSet:
                Local = os.path.join(LocalDir, file)
                logger.info(self.ftp.nlst(file))
                if file.find(".") == -1:
                    if not os.path.exists(Local):
                        os.makedirs(Local)
                    self.DownLoadFileTrees(Local, file)
                else:
                    self.DownLoadFile(Local, file)
            self.ftp.cwd("..")
            put(set(RemoteNames))
            return newSet

    def close(self):
        self.ftp.quit()
