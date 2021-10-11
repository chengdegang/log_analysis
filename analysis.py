import argparse
import pdb
import re
import datetime
import csv
import sys
import time
from time import sleep
from tqdm import tqdm

class Deal_data():
    def read(self,file):
        """
        :param file: 需要处理的文件路径
        :return: 一个处理完成的列表
        """
        result_data = []
        with open(file) as ces:
            read = ces.readlines()
            time1 = []
            time2 = []
            for line in read:
                # 遍历每行添加处理,把每行加到后面
                # pline +=  line.rstrip()
                # 打印每一行
                # print(line.strip())
                # 找到两个时间并相减
                if 'time1' in line:
                    # time_ori1 = line.split('time1')
                    # 正则提取time1与s之间的数
                    time_ori1 = re.findall(r"time1=(.+?)s", line)
                    # 去掉列表括号
                    time_ori1_ = ''.join(time_ori1)
                    # print(time_ori1_)
                    time1.append(time_ori1_)
                if 'time2' in line:
                    # time_ori1 = line.split('time1')
                    # 正则提取time1与s之间的数
                    time_ori2 = re.findall(r"time2=(.+?)s", line)
                    time_ori2_ = ''.join(time_ori2)
                    # print(time_ori2_)
                    time2.append(time_ori2_)
        # print(time1)
        # 字符串列表转为float列表
        num_time1 = list(map(float, time1))
        num_time2 = list(map(float, time2))
        # print(num_time1)
        # print(num_time2)
        # 处理拿到的time1、2
        values = [num_time2[i] - num_time1[i] for i in range(len(num_time1))]
        # 统一处理value为小数点后三位
        for i in range(len(values)):
            # print(float('%.4f' % values[i]))
            result_data.append(float('%.3f' % values[i]))
        # print(len(result_data))
        print(result_data)
        return result_data

    # 结果写入txt
    def write_txt(self,list):
        # time_stamp = '{0:%Y%m%d%H%M%S}'.format(datetime.datetime.now())
        writefile = f'data/result666.txt'
        with open(writefile, 'w') as wf:
            # wf.write('T2-T1时间差' + '\n')
            for wline in list:
                print(wline)
                wf.write(str(wline) + '\n')

    # 结果写入csv
    def write_csv(self,file='data/test.csv'):
        headers = ['header1', 'header2', 'header3', 'header4', 'header5']
        rows = [
            [1, 'xiaoming', 'male', 168, 23],
            [2, 'xiaohong', 'female', 162, 22],
            [3, 'xiaozhang', 'female', 163, 21],
        ]
        with open(file, 'w')as f:
            f_csv = csv.writer(f)
            f_csv.writerow(headers)
            f_csv.writerows(rows)

    def external(self):
        """
        :return:
        通过sh文件指定运行
        """
        ext = argparse.ArgumentParser()
        ext.add_argument('--filename', required=True)
        exts = ext.parse_args()
        return exts

def judge(str1,str2):
    #替换掉两个字符串中所有的空格
    str1 = str1.replace(' ','')
    str2 = str2.replace(' ','')
    if str1 == str2:
        print("{:*{}66}".format(f'  对比内容完全相同  ', '^'))
    else:
        if len(str1) == len(str2):
            str1l = []
            str2l = []
            for i, str in enumerate(str1):
                str1l.append(str)
            for i, str in enumerate(str2):
                str2l.append(str)
            n = 0
            for s1 in str1l:
                if s1 != str2l[n]:
                    print(f'find diff is {s1} , no [{n+1}]')
                n = n + 1
        else:
            print("{:*{}66}".format(f'  对比内容不相同  ', '^'))

class Deal_ylog():
    # pdb.set_trace()
    def read(self,file,infopic='2021-09-29-10-48-50'):
        # 读取所有指定文本格式内的内容
        result = []
        with open(file) as f:
            read = f.read()
            comment1 = re.compile(r'xxxx(.+?)xxxx', re.S)
            comment2 = re.compile(r'DeviceInfo(.+?)End Loc=========================', re.S)
            res = comment2.findall(read)
            # print(res[4])
            # 在所有指定文本格式内的内容查找符合条件的
            match = f'{infopic}_Suc.jpg'
            for data in res:
                if match in data:  # _Fail  _Suc
                    # print(data)
                    needdata1 = re.findall(r"cam_intri: (.+?)\n", data)  # ??
                    # needdata1 = f'ur input:{match}\ncam_intri: {needdata1[0]}'
                    result.append(f'ur input:{match}')
                    result.append(f'cam_intri: {needdata1[0]}')
                    print(f'\n{result[0]}\n{result[1]}')
                    needdata2 = re.findall(r"cam_intri: (.+?)\n", data)
        return result

    def external(self):
        """
        :return:
        通过sh文件指定运行
        """
        ext = argparse.ArgumentParser()
        ext.add_argument('--file', required=True)
        # ext.add_argument('--infopic', required=True)
        exts = ext.parse_args()
        return exts

if __name__ == '__main__':
    #测试部分
    # data = testylog.read(file='data/ylog.txt',infopic='2021-09-29-10-48-50')

    #正式运行代码
    testylog = Deal_ylog()
    file = str(sys.argv[1])
    infopic = str(sys.argv[2])
    for i in tqdm(range(20)):
        sleep(0.1)
    data = testylog.read(file=file,infopic=infopic)
    # data = testylog.read(testylog.external())

    # test = Deal_data()  #写数据到指定文件中
    # test.write_txt(data)



    # 可配置时调用函数
    # list= read(external())
    # Deal_data.write_txt(Deal_data.read(file))
    # 以下为测试
    # write_csv()
    # ss = '引起报错的函数foo   参数较多，代码中已经用了换行。这样导致报错'
    # print(ss.replace(' ',''))

    # judge('引起报错的函数foo   参数较多，代码中已经用了换行。这样导致报错','引起报2的函数foo参数较多，代码  中已经用了换行。这样导致报错')




