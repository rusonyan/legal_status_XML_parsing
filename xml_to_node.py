# conding=utf8
import os

import xmltodict
from loguru import logger

import toast
from node import node_parse

"""
XML节点组分拆
"""


def locate_XML_file(path):
    g = os.walk(path)
    all_file_list = []
    for path, dir_list, file_list in g:
        for file_name in file_list:
            all_file_list.append(os.path.join(path, file_name))

    return find_target_xml(all_file_list)


def find_target_xml(all_file_list, count=0):
    for file in all_file_list:
        if file.endswith(".XML"):
            with open(file, "r", encoding="UTF-8") as f:
                xml = f.read()
                try:
                    doc = xmltodict.parse(xml)
                except Exception as e:
                    toast.send_errow("XML文件出错,文件打开失败！", str(e))
                if "business:PRS" in doc.keys():
                    logger.info(file)
                    doc_data = doc["business:PRS"]["business:PRSRecord"]
                    count += node_parse(doc_data)
    return count
