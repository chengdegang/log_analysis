import argparse
import re
import datetime
import csv

file = 'ces.txt'

def read(file):
    result_data = []
    with open(file) as ces:
        read = ces.readlines()
        time1 = []
        time2 = []
        for line in read:
            # 遍历每行添加处理,把每行加到后面
            # pline +=  line.rstrip()
            #打印每一行
            # print(line.strip())
            #找到两个时间并相减
            if 'time1' in line:
                # time_ori1 = line.split('time1')
                #正则提取time1与s之间的数
                time_ori1 = re.findall(r"time1=(.+?)s", line)
                #去掉列表括号
                time_ori1_ = ''.join(time_ori1)
                # print(time_ori1_)
                time1.append(time_ori1_)
            if 'time2' in line:
                # time_ori1 = line.split('time1')
                #正则提取time1与s之间的数
                time_ori2 = re.findall(r"time2=(.+?)s", line)
                time_ori2_ = ''.join(time_ori2)
                # print(time_ori2_)
                time2.append(time_ori2_)
    # print(time1)
    #字符串列表转为float列表
    num_time1 = list(map(float, time1))
    num_time2 = list(map(float, time2))
    # print(num_time1)
    # print(num_time2)

    #处理拿到的time1、2
    values = [num_time2[i] - num_time1[i] for i in range(len(num_time1))]
    #统一处理value为小数点后三位
    for i in range(len(values)):
        # print(float('%.4f' % values[i]))
        result_data.append(float('%.3f' % values[i]))
    # print(len(result_data))
    print(result_data)
    return result_data

#结果写入txt
def write_txt(list):
    # time_stamp = '{0:%Y%m%d%H%M%S}'.format(datetime.datetime.now())
    writefile = f'data/result.txt'
    with open(writefile,'w') as wf:
        wf.write('T2-T1时间差'+'\n')
        for wline in list:
            print(wline)
            wf.write(str(wline)+'\n')

# 结果写入csv
def write_csv():
    headers = ['header1', 'header2', 'header3', 'header4', 'header5']
    rows = [
        [1, 'xiaoming', 'male', 168, 23],
        [2, 'xiaohong', 'female', 162, 22],
        [3, 'xiaozhang', 'female', 163, 21],
    ]
    with open('data/test.csv', 'w')as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)

"""
通过sh文件指定运行
"""
def external():
    ext = argparse.ArgumentParser()
    ext.add_argument('--filename', required=True)
    exts = ext.parse_args()
    return exts
# read(file)

#可配置时调用函数
# list= read(external())
write_txt(read(file))

#以下为测试
# write_csv()
