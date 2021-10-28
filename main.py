# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sys


class testc():
    def __init__(self):
        print('init~~~')
        self.version = 'v2'

    def test1(self,a=1,b=2):
        c = a+ b
        print(c)
    def test2(self):
        print('666')
    def test3(self):
        header = {
            "content-type":"application/json",
            # self.appId:self.appId,
            # self.nonce:self.nonce,
            # self.timestamp:self.timestamp,
            # self.sign:self.sign,
            'version':self.version
        }
        data = {
            "version":self.version
        }
        print(header)
        print(data)

def test2(ff):
    attention =[]
    info = ff.split("/")[-1:][0]
    attention.append(info)
    print(attention)



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def sendmail(mesg):
    mesg_2 = ''
    for i in range(len(mesg)):
        mesg_2 = mesg_2 + mesg[int(i)] + '\n'
    print(mesg_2)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # mytest = testc()
    # mytest.test1(a=2,b=3)
    # mytest.test2()
    # mytest.test3()
    # print_hi('PyCharm')
    # print(sys.argv)
    # print(sys.argv[1])
    result2 = ['riqi  zhuti 22','riqi  zhuti 33']
    atte = ['file1','file2']
    sendmail(mesg=result2 + ['\n','以下是找到的需要关注的文件'] + atte)

    # test2('/Users/jackrechard/PycharmProjects/crawl_syb/download/2021-10-25/2021年杭州西湖区住房和城乡建设局招聘编外合同制人员公告.xlsx')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
