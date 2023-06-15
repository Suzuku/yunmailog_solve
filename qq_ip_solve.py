# import numpy as np
import pandas as pd
import shutil
import os
import time
from datetime import datetime


# 计算两个日期时间字符串间隔
def calDateStrInterval(str1, str2):
    # 先格式化为timestamp
    timestamp1 = datetime.strptime(str1, '%Y-%m-%d %H:%M:%S').timestamp()
    timestamp2 = datetime.strptime(str2, '%Y-%m-%d %H:%M:%S').timestamp()
    return abs(timestamp1-timestamp2)

# 对单个文件进行清洗并生成excel


def cleanSingleFile(fileName):
    path = r'./%s.xls' % fileName
    dataFrame = pd.read_excel(path)
# 构造一个dict来放简化的数据，省的dataframe遍历太复杂了
    dict = {}
    # 批量处理给dict赋值
    for row_index, row in dataFrame.iterrows():
        dict[row_index] = {'ip': row['登录IP'], 'time': row['截获时间']}
    # 记一个对象，值为第一个
    firstObj = ''
    # 存储需要被删除的列
    deleteCol = {}
    # 存储结果数据
    resultFrame = []
    # 接下来处理dict即可
    for index, content in dict.items():
        if index == 0:
            firstObj = {'time': dict[0]['time'], 'ip': dict[0]['ip']}
        elif firstObj['ip'] == content['ip'] and calDateStrInterval(firstObj['time'], content['time']) < 3600:
            deleteCol[index] = {'time': content['time'],
                                'ip': content['ip']}
        else:
            firstObj = {'time': content['time'], 'ip': content['ip']}

    # 进行删除操作
    for colIndex, colContent in deleteCol.items():
        dataFrame.drop([colIndex], inplace=True)

    dataFrame.to_excel('./登录日志清洗后/%s【清洗后】.xlsx' % fileName, index=False)


# main
if __name__ == '__main__':
    start_time = time.time()
    print('运行中，请稍等.........')
    # 如果存在就删掉否则新建，不然每次需要删掉文件夹才能运行
    if os.path.exists('./登录日志清洗后'):
        shutil.rmtree('./登录日志清洗后')
    os.makedirs('./登录日志清洗后')
    path = os.curdir
    files = [f for f in os.listdir() if os.path.isfile(f)]
    for file in files:
        fileName = file.split('.')[0]
        if fileName.find('登录日志同步') >= 0:
            cleanSingleFile(fileName)
    print('程序运行耗时：%s' % (time.time() - start_time))

# 无糖浏览器可以批量查IP的归属地信息 单次最大支持1000条
