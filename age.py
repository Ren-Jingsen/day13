from  unittest import  TestCase
from  demo import Calc

class TestCalc(TestCase):

    def testAdd1(self):
        #1.造数据
        a = 2
        b = 3
        c = 5
        #2.开始测试
        calc = Calc()
        sum = calc.add(a,b)

        #3.将实际结果与期望结果进行对比

        self.assertEqual(c,sum)

    def testAdd2(self):
        # 1.造数据
        a = 6
        b = -7
        c = -1

        # 2.开始测试
        calc = Calc()
        sum = calc.add(a, b)

        # 3.将实际结果与期望结果进行比对
        self.assertEqual(c, sum)

    def testAdd3(self):
        # 1.造数据
        a = -6
        b = 7
        c = 1

        # 2.开始测试
        calc = Calc()
        sum = calc.add(a, b)

        # 3.将实际结果与期望结果进行比对
        self.assertEqual(c, sum)

    def testAdd4(self):
        # 1.造数据
        a = -6
        b = -7
        c = -13

        # 2.开始测试
        calc = Calc()
        sum = calc.add(a, b)

        # 3.将实际结果与期望结果进行比对
        self.assertEqual(c, sum)

    def testAdd5(self):
        # 1.造数据
        a = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        b = 7
        c = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000007

        # 2.开始测试
        calc = Calc()
        sum = calc.add(a, b)

        # 3.将实际结果与期望结果进行比对
        self.assertEqual(c, sum)