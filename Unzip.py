import os
import zipfile

from loguru import logger
'''
批量文件夹解压
'''


def unzip_file(path):  # 获取目录下所有文件名
    for filename in os.listdir(path):  # 由于这里是当前路径，所以需要把这个代码文件和你要处理的文件放到同一个文件夹里
        if filename.endswith('.ZIP'):
            filepath = os.path.join(path, filename)
            zip_file = zipfile.ZipFile(filepath)  # 获取压缩文件
            logger.info("解压"+filename)
            newfilepath = filename.split(".", 1)[0]  # 获取压缩文件的文件名
            newfilepath = os.path.join(path, newfilepath)
            if os.path.isdir(newfilepath):  # 根据获取的压缩文件的文件名建立相应的文件夹
                pass
            else:
                os.mkdir(newfilepath)
            for name in zip_file.namelist():  # 解压文件
                zip_file.extract(name, newfilepath)
            zip_file.close()
            logger.info("解压{0}成功".format(filename))
