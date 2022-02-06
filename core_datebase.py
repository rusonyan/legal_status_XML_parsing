import re

from DB import spilt_address

'''
入库函数
'''


def storage_summary_table(db, code, data, p_num, text, before=None, after=None):
    db.cursor.execute(
        'INSERT INTO patent_change_log (id, code, before_change, after_change, '
        'pub_date, patent_num, raw_data,change_id, source)'
        'values (%s,%s,%s,%s,%s,%s,%s,%s,%s);',
        (0, code, before, after, data, p_num, text, db.back()[0], db.publishTime))


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
    storage_summary_table(db, code, data, p_num, text)


def dd_insert(db, code, p_num, text, result):
    db.cursor.execute('INSERT INTO dd VALUES (%s,%s,%s,%s,%s)',
                      (0, p_num, result[0], result[1], db.publishTime))
    storage_summary_table(db, code, db.publishTime, p_num, text)


def ip_insert(db, code, p_num, text, result):
    if len(result) < 4:
        pass
    else:
        db.cursor.execute(
            'INSERT INTO ip (id, patent_id, decision_num, decision_date, commission_num, conclusion) '
            'values (%s,%s,%s,%s,%s,%s);',
            (0, p_num, result[0], result[1], result[2], result[3]))
        storage_summary_table(db, code, result[1], p_num, text)


def ee_insert(db, code, p_num, text, result):
    db.cursor.execute(
        'INSERT INTO ee (id, patent_id, contract, giver, assignee, product_name, license_type, pub_date)'
        'VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
        (0, p_num, result[0], result[1], result[2], result[3], result[4], result[5]))
    storage_summary_table(db, code, result[5], p_num, text)


def ec_insert(db, code, p_num, text, result):
    db.cursor.execute('INSERT INTO ec VALUES (%s,%s,%s,%s,%s,%s)',
                      (0, p_num, result[0], result[1], result[2], result[3]))
    storage_summary_table(db, code, result[3], p_num, text)


def pe_insert(db, code, p_num, text, result):
    db.cursor.execute('INSERT INTO pe (id, patent_id, license_num, pub_date, pledger, pledgee, product_name)'
                      'VALUES (%s,%s,%s,%s,%s,%s,%s)',
                      (0, p_num, result[0], result[1], result[2], result[3], result[4]))
    storage_summary_table(db, code, result[1], p_num, text)


def pm_insert(db, code, p_num, text, result):
    db.cursor.execute('INSERT INTO pm (id, patent_id, contract, pub_date, matter, before_change, after_change)'
                      'VALUES (%s,%s,%s,%s,%s,%s,%s)',
                      (0, p_num, result[0], result[1], result[2], result[3], result[4]))
    storage_summary_table(db, code, result[1], p_num, text)


def pc_insert(db, code, p_num, text, result):
    db.cursor.execute('INSERT INTO pc VALUES (%s,%s,%s,%s,%s,%s)',
                      (0, p_num, result[0], result[1], result[2], result[3]))
    storage_summary_table(db, code, result[3], p_num, text)


def rr_insert(db, code, p_num, text, result):
    db.cursor.execute('INSERT INTO rr VALUES (%s,%s,%s,%s,%s)',
                      (0, p_num, result[0], result[1], db.publishTime))
    storage_summary_table(db, code, db.publishTime, p_num, text)


def tr_insert(db,
              code,
              p_num,
              text,
              result,
              before_owner=None,
              after_owner=None,
              before_co_patent_holder='',
              after_co_patent_holder=''
              ):
    before_owner = result[2]
    after_owner = result[3]
    if len(result) == 10:
        if match(result[8], r'变更前权利人:(.*)') is not None:
            before_co_patent_holder = match(result[8], r'变更前权利人:(.*)')
        if match(result[9], r'变更后权利人:(.*)') is not None:
            after_co_patent_holder = match(result[9], r'变更后权利人:(.*)')

    address = spilt_address(result[6])
    if address[4] is not None:
        abcode = int(address[4])
    else:
        abcode = None
    db.cursor.execute(
        'INSERT INTO tr VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
        (0, p_num, before_owner, before_co_patent_holder, after_owner, after_co_patent_holder, result[5], result[6],
         result[0], db.publishTime,
         abcode, address[0], address[1], address[2], address[3]))
    storage_summary_table(db,
                          code,
                          db.publishTime,
                          p_num,
                          text,
                          before=before_owner + ';' + before_co_patent_holder + '\n' + result[5],
                          after=after_owner + ';' + after_co_patent_holder + '\n' + result[6])


def cp_insert(db,
              code,
              p_num,
              text,
              result,
              before_owner=None,
              after_owner=None,
              before_co_patent_holder='',
              after_co_patent_holder=''):
    before_owner = result[1]
    after_owner = result[2]
    if len(result) == 9:
        if match(result[7], r'变更前:(.*)') is not None:
            before_co_patent_holder = match(result[7], r'变更前:(.*)')
        if match(result[8], r'变更后:(.*)') is not None:
            after_co_patent_holder = match(result[8], r'变更后:(.*)')
    address = spilt_address(result[5])
    if address[4] is not None:
        abcode = int(address[4])
    else:
        abcode = None
    db.cursor.execute(
        'INSERT INTO cp VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
        (0, p_num, before_owner, before_co_patent_holder, after_owner, after_co_patent_holder, result[4], result[5],
         db.publishTime, None, abcode, address[0], address[1], address[2], address[3]))
    storage_summary_table(db,
                          code,
                          db.publishTime,
                          p_num,
                          text,
                          before=before_owner + '\n' + result[4],
                          after=after_owner + ';' + after_co_patent_holder + '\n' + result[5]
                          )
