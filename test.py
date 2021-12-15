import time
from loguru import logger
from Unzip import unzip_file
from xml_to_node import locate_XML_file

import pickle
# locate_XML_file(r'C:/Users/ruson/Desktop/法律状态/XML数据/')

# def get():
#     with open('.history', 'rb') as f:
#         return pickle.load(f)
        
# a=list(get())
# a.sort()
# print(a)


# Local = r'/home/yrs/history/20211116/'

# import os
# files=os.listdir(Local)
# files.sort()

# for file in files:
#     path=os.path.join(Local,file)
#     print(path)
#    #unzip_file(path)
#     locate_XML_file(path)

def put(tuple):
    with open('.history', 'wb') as f:
        pickle.dump(tuple, f)


def get():
    with open('.history', 'rb') as f:
        return pickle.load(f)

a=list(get())
a.sort()
print(a)

# a=a[:-2]
# print(a)
# b=set(a)
# print(b)
# put(b)