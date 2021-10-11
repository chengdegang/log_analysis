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

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # mytest = testc()
    # mytest.test1(a=2,b=3)
    # mytest.test2()
    # mytest.test3()
    # print_hi('PyCharm')
    print(sys.argv)
    print(sys.argv[1])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
