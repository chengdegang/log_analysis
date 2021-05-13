import argparse
import re
import datetime

# file = 'ces.txt'

def read(exts):
    with open(exts.filename) as ces:
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
    value = [num_time2[i] - num_time1[i] for i in range(len(num_time1))]
    print(value)
    return value

def write(list):
    time_stamp = '{0:%Y%m%d%H%M%S}'.format(datetime.datetime.now())
    writefile = f'data/result_{time_stamp}.txt'
    with open(writefile,'a') as wf:
        for wline in list:
            print(float('%.3f' % wline))
            wf.write(str(float('%.3f' % wline))+'\n')

# read('ces.txt')
def external():
    ext = argparse.ArgumentParser()
    ext.add_argument('--filename', required=True)
    exts = ext.parse_args()
    return exts

list= read(external())
write(list)
# write(read('ces.txt'))
