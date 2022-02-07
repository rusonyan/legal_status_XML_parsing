import os

from loguru import logger

from xml_to_node import locate_XML_file

'''
批量处理XML
'''

Local = r'/root/文档/xml/'

if __name__ == '__main__':
    files = os.listdir(Local)
    files.sort()
    for file in files:
        path = os.path.join(Local, file)
        logger.debug(path)
        # unzip_file(path)
        locate_XML_file(path)
