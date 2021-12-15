from DB import spilt_address
import re
'''
入库函数
'''


def insert(db, code, after, data, p_num, text, before=None):
    db.cursor.execute(
        'INSERT INTO `ls.statechange` VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
        (0, code, before, after, data, p_num, text, db.back()[0]))


def match(line, rule):
    try:
        return re.match(rule, line).group(1)
    except AttributeError:
        return None


def direct_insert(db, code, p_num, text, result):
    if code == 'CF01' or code == 'CX01':
        data = db.publishTime
    else:
        data = result[1]
    insert(db, code, result[0], data, p_num, text)


def dd_insert(db, code, p_num, text, result):
    db.cursor.execute('INSERT INTO `ls.dd` VALUES (%s,%s,%s,%s,%s)',
                      (0, p_num, result[0], result[1], db.publishTime))
    insert(db, code, '文件的公告送达', db.publishTime, p_num, text)


def ip_insert(db, code, p_num, text, result):
    if len(result) < 4:
        pass
    else:
        db.cursor.execute(
            'INSERT INTO `ls.ip` VALUES (%s,%s,%s,%s,%s,%s)',
            (0, p_num, result[0], result[1], result[2], result[3]))
        insert(db, code, '专利权部分无效', result[1], p_num, text)


def ee_insert(db, code, p_num, text, result):
    db.cursor.execute(
        'INSERT INTO `ls.ee` VALUES (%s,%s,%s,%s,%s,%s,%s)',
        (0, p_num, result[0], result[1], result[2], result[3], result[4]))
    insert(db, code, '专利实施许可合同备案的生效', result[4], p_num, text)


def ec_insert(db, code, p_num, text, result):
    db.cursor.execute('INSERT INTO `ls.ec` VALUES (%s,%s,%s,%s,%s,%s)',
                      (0, p_num, result[0], result[1], result[2], result[3]))
    insert(db, code, '专利实施许可合同备案的注销', result[3], p_num, text)


def pe_insert(db, code, p_num, text, result):
    db.cursor.execute('INSERT INTO `ls.pe` VALUES (%s,%s,%s,%s,%s,%s)',
                      (0, p_num, result[0], result[1], result[2], result[3]))
    insert(db, code, '专利权质押合同登记的生效', result[1], p_num, text)


def pm_insert(db, code, p_num, text, result):
    db.cursor.execute('INSERT INTO `ls.pm` VALUES (%s,%s,%s,%s,%s,%s)',
                      (0, p_num, result[0], result[1], result[2], result[3]))
    insert(db, code, '专利权质押合同登记的变更', result[0], p_num, text)


def pc_insert(db, code, p_num, text, result):
    db.cursor.execute('INSERT INTO `ls.pc` VALUES (%s,%s,%s,%s,%s,%s)',
                      (0, p_num, result[0], result[1], result[2], result[3]))
    insert(db, code, '专利权质押合同登记的注销', result[3], p_num, text)


def rr_insert(db, code, p_num, text, result):
    db.cursor.execute('INSERT INTO `ls.rr` VALUES (%s,%s,%s,%s,%s)',
                      (0, p_num, result[0], result[1], db.publishTime))
    insert(db, code, '权利的恢复', db.publishTime, p_num, text)


def tr_insert(db,
              code,
              p_num,
              text,
              result,
              before_owner=None,
              after_owner=None):
    if len(result) == 10:
        if match(result[8], r'变更前权利人:(.*)') is not None:
            before_owner = result[2] + ';' + match(result[8], r'变更前权利人:(.*)')
        if match(result[9], r'变更后权利人:(.*)') is not None:
            after_owner = result[3] + ';' + match(result[9], r'变更后权利人:(.*)')
    elif len(result) == 7:
        before_owner = result[2]
        after_owner = result[3]
    else:
        raise Exception('专利转移解析器无匹配模板', text)

    address = spilt_address(result[6])
    db.cursor.execute(
        'INSERT INTO `ls.tr` VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
        (0, p_num, before_owner, after_owner, result[5], result[6], result[0],
         None, address[0], address[1], address[2], address[3]))
    insert(db,
           code,
           after_owner + '\n' + result[6],
           db.publishTime,
           p_num,
           text,
           before=before_owner + '\n' + result[5])


def cp_insert(db,
              code,
              p_num,
              text,
              result,
              before_owner=None,
              after_owner=None):
    if len(result) == 9:
        if match(result[7], r'变更前:(.*)') is not None:
            before_owner = result[1] + ';' + match(result[7], r'变更前:(.*)')
        if match(result[8], r'变更后:(.*)') is not None:
            after_owner = result[2] + ';' + match(result[8], r'变更后:(.*)')
    elif len(result) == 6:
        before_owner = result[1]
        after_owner = result[2]
    else:
        raise Exception('专利人更名器无匹配模板', text)

    address = spilt_address(result[5])
    db.cursor.execute(
        'INSERT INTO `ls.cp` VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
        (0, p_num, before_owner, after_owner, result[4], result[5],
         db.publishTime, None, address[0], address[1], address[2], address[3]))
    insert(db,
           code,
           after_owner + '\n' + result[5],
           db.publishTime,
           p_num,
           text,
           before=before_owner + '\n' + result[4])
