import unittest
from analysis import judge

class Test(unittest.TestCase):
    def setUp(self):
        1

    def tearDown(self):
        2
        # print("{:*{}25}".format('测试完成','^'))

    def test_1(self):
        self.str1 = '测试测试文字1111'
        self.str2 = '测试测试文字1111'
        res = judge(self.str1,self.str2)
        self.assertEqual(res, '***************************  对比内容完全相同  ***************************')

    def test_2(self):
        self.str1 = '测试测试文字1111'
        self.str2 = '测试测试文字1112'
        res = judge(self.str1,self.str2)
        self.assertEqual(res, '***************************  对比内容完全相同  ***************************')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test('test_1'))
    suite.addTest(Test('test_2'))

    runner = unittest.TextTestRunner()
    runner.run(suite)