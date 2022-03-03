import ftplib
import os
import pickle

from loguru import logger

from config import FTP_CONFIG

"""
FTP类
"""


def history_add(str):
    history = get()
    history.add(str)
    with open(".history", "wb") as f:
        pickle.dump(history, f)


def put(already_tuple):
    with open(".history", "wb") as f:
        pickle.dump(already_tuple, f)


def get():
    with open(".history", "rb") as f:
        return pickle.load(f)


class Ftp:
    ftp = ftplib.FTP()

    def __init__(self, Local, Remote):
        self.ftp.set_debuglevel(2)
        self.Local = Local
        self.Remote = Remote
        self.ftp.encoding="gbk"
        self.ftp.connect(host=FTP_CONFIG[0]["host"], port=21,timeout=1200)
        self.ftp.login(FTP_CONFIG[0]["username"], FTP_CONFIG[0]["password"])

    def login(self):
        self.ftp.connect(FTP_CONFIG[0]["host"], 21,timeout=1200)
        self.ftp.login(FTP_CONFIG[0]["username"], FTP_CONFIG[0]["password"])

    def close(self):
        self.ftp.quit()
        logger.info("ftp退出")

    def find_raw_data(self,RemoteNames=[]):
        self.ftp.cwd(self.Remote)
        mlsd = self.ftp.mlsd()
        for m in mlsd:
            RemoteNames.append(m[0])
        newSet = set(RemoteNames) - get()
        logger.debug("远程服务器的所有文件列表:" + str(RemoteNames))
        logger.debug("本次要下载的文件列表:" + str(newSet))
        # put(set(RemoteNames))
        # newSet=set(RemoteNames)-set(RemoteNames)
        new_list = list(newSet)
        new_list.sort()
        if len(new_list) is 0:
            return None
        else:
            return new_list

    def download_file(self, LocalFile, RemoteFile):
        file_handler = open(LocalFile, "wb")
        logger.info(file_handler)
        self.ftp.retrbinary("RETR " + RemoteFile, file_handler.write)
        file_handler.close()
        logger.info("下载完成")
        return True

    def download_folder(self, LocalDir, folder):
        RemoteDir = os.path.join(self.Remote, folder)
        if not os.path.exists(LocalDir):
            os.makedirs(LocalDir)
        self.ftp.cwd(RemoteDir)
        RemoteNames = self.ftp.nlst()
        logger.info(folder + "的文件夹文件列表:" + str(RemoteNames))
        for file in RemoteNames:
            Local = os.path.join(LocalDir, file)
            if file.endswith(".ZIP"):
                logger.info("正在下载:" + file)
                if self.download_file(Local, file):
                    history_add(folder)


if __name__ == "__main__":
    history_add(".")
    already_list = list(get())
    already_list.sort()
    print(already_list)
