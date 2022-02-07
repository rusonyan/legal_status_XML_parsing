import os
import zipfile

from loguru import logger

"""
批量文件夹解压
"""


def unzip_file(path):
    for filename in os.listdir(path):
        if filename.endswith(".ZIP"):
            filepath = os.path.join(path, filename)
            zip_file = zipfile.ZipFile(filepath)
            logger.info("解压" + filename)
            newfilepath = filename.split(".", 1)[0]
            newfilepath = os.path.join(path, newfilepath)
            if os.path.isdir(newfilepath):
                pass
            else:
                os.mkdir(newfilepath)
            for name in zip_file.namelist():
                zip_file.extract(name, newfilepath)
            zip_file.close()
            logger.info("解压{0}成功".format(filename))
