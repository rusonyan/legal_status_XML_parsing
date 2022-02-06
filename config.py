from core_datebase import *

'''
程序配置
'''

MAX_RETRY = 4  # 每日最大重连次数
MINI_CONNECT_TIME = 50  # 每次重新请求间隔的最短时间(单位:秒)
MAX_CONNECT_TIME = 200  # 每次重新请求间隔的最长时间(单位:秒)
UNRESOLVED_STATUS_CODE = ('CB', 'GR', 'CD')  # 不予处理的法律状态类型
LOCAL_FOLDER = r'C:\Users\ruson\Desktop\XML数据\20210212'  # 存放本地XML的文件夹
REMOTE_FOLDER = r"SIPO/CN-PA-PRSS-30 中国外观设计专利法律状态标准化数据/".encode("utf-8").decode(
    "latin1"
)  # FTP服务端远程文件夹

"""
解析模板配置
"""
MODEL = {
    'TR01': {
        're': [
            r'登记生效日:(\d{8})', r'变更事项:(.*)', r'变更前权利人:(.*)', r'变更后权利人:(.*)',
            r'变更事项:(.*)', r'变更前权利人:(.*)', r'变更后权利人:(.*)', r'变更事项:(.*)',
            r'(变更前权利人:.*)', r'(变更后权利人:.*)'
        ],
        'fun':
            tr_insert,
    },
    'CP01': {
        're': [
            r'变更事项:(.*)', r'变更前:(.*)', r'变更后:(.*)', r'变更事项:(.*)', r'变更前:(.*)',
            r'变更后:(.*)', r'变更事项:(.*)', r'(变更前:.*)', r'(变更后:.*)'
        ],
        'fun':
            cp_insert,
    },
    'CP02': {
        're': [
            r'变更事项:(.*)', r'变更前:(.*)', r'变更后:(.*)', r'变更事项:(.*)', r'变更前:(.*)',
            r'变更后:(.*)', r'变更事项:(.*)', r'(变更前:.*)', r'(变更后:.*)'
        ],
        'fun':
            cp_insert,
    },
    'CP03': {
        're': [
            r'变更事项:(.*)', r'变更前:(.*)', r'变更后:(.*)', r'变更事项:(.*)', r'变更前:(.*)',
            r'变更后:(.*)', r'变更事项:(.*)', r'(变更前:.*)', r'(变更后:.*)'
        ],
        'fun':
            cp_insert,
    },
    'IP01': {
        're':
            [r'无效宣告决定号:(.*)', r"无效宣告决定日:(\d{8})", r'委内编号:(.*)', r'审查结论:(.*)'],
        'fun': ip_insert,
    },
    'DD01': {
        're': [r'收件人:(.*)', r'文件名称:(.*)'],
        'fun': dd_insert,
    },
    'EE01': {
        're': [
            r'合同备案号:(.*)', r'让与人:(.*)', r'受让人:(.*)', r'使用外观设计的产品名称:(.*)', r'许可种类:(.*)',
            r'备案日期:(\d{8})'
        ],
        'fun':
            ee_insert,
    },
    'EC01': {
        're': [r'合同备案号:(.*)', r'让与人:(.*)', r'受让人:(.*)', r'解除日:(\d{8})'],
        'fun': ec_insert,
    },
    'PE01': {
        're': [r'登记号:(.*)', r'登记生效日:(\d{8})', r'出质人:(.*)', r'质权人:(.*)', r'使用外观设计的产品名称:(.*)'],
        'fun': pe_insert,
    },
    'PM01': {
        're': [r'登记号:(.*)', r'变更日:(\d{8})', r'变更事项:(.*)', r'变更前:(.*)', r'变更后:(.*)'],
        'fun': pm_insert,
    },
    'PC01': {
        're': [r'登记号:(.*)', r'出质人:(.*)', r'质权人:(.*)', r'解除日:(\d{8})'],
        'fun': pc_insert,
    },
    'RR01': {
        're': [r'原决定名称:(.*)', r'原决定公告日:(\d{8})'],
        'fun': rr_insert,
    },
    'AV01': {
        're': [r'(.*)', r"放弃生效日:(\d{8})"],
        'fun': direct_insert,
    },
    'CF01': {
        're': [r'(.*)'],
        'fun': direct_insert,
    },
    'CX01': {
        're': [r'(.*)'],
        'fun': direct_insert,
    },
    'IW01': {
        're': [r'(.*)', r"无效宣告决定日:(\d{8})"],
        'fun': direct_insert,
    },
    'PP01': {
        're': [r'(.*)', r"登记生效日:(\d{8})"],
        'fun': direct_insert,
    },
    'PD01': {
        're': [r'(.*)', r"解除日:(\d{8})"],
        'fun': direct_insert,
    }
}
