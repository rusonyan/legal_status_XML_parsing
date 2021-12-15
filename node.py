import re
from datetime import datetime

from loguru import logger

import config
import toast
from DB import DB
''' 
模板解析器:
在更改数据之前加索引：
ALTER TABLE `patent.patent` ADD INDEX  ar_doc_num_index(`ar_doc_num`)
'''

UNRESOLVED_STATUS_CODE = ('CB', 'GR', 'CD')


def checks(num):
    value = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    check_code = 0
    for x, y in zip(value, num):
        check_code = check_code + x * int(y)
    return 'ZL ' + num + '.' + str(
        (check_code % 11)) if (check_code % 11) != 10 else 'X'


def check(db, num):
    db.cursor.execute("""  SELECT id from `patent.patent`
            where ar_doc_num="%s" """ % (num))
    id_resultss = db.cursor.fetchall()
    if num is not None and len(id_resultss) > 0:
        return id_resultss[0][0]
    else:
        raise ValueError('未找到ID ' + num)


def match(line, rule):
    try:
        return re.match(rule, line).group(1)
    except AttributeError:
        return None


def handle(lines, rules, result, i=0, j=0):
    while i < len(lines) and j < len(rules):
        m = match(lines[i], rules[j])
        if m is not None:
            result.append(m)
            j = j + 1
        i = i + 1
    return result


def temp(db, code, p_num, text):
    try:
        config.MODEL[code]['fun'](db, code, p_num, text,
                                  handle(text.splitlines(),
                                         config.MODEL[code]['re'], []))
    except ValueError as e:
        logger.error(e)


def node_parse(node):
    s = ''
    db = DB(node[0]['business:PRSPublicationDate']['base:Date'])
    try:
        for d in node:
            if d['business:PRSCode'] in config.MODEL:
                temp(
                    db, d['business:PRSCode'],
                    d['business:ApplicationReference'][0]['base:DocumentID']
                    ['base:DocNumber'], d['business:PRSInformation'])
            elif d['business:PRSCode'][:2] in UNRESOLVED_STATUS_CODE:
                pass
            else:
                s = s + d['business:PRSCode'] + '\n' + d[
                    'business:PRSInformation']
    except Exception as e:
        db.cn.rollback()
        toast.send_errow('数据库插入发生错误', str(e))
    else:
        db.cn.commit()
    finally:
        db.cursor.execute('INSERT INTO `ls.dblog`  VALUES (%s,%s,%s,%s)',
                          (0, datetime.now(), db.publishTime, None))
        db.cn.commit()
    if len(s) > 0:
        toast.send("发现一个新表头", s)
